# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:35:18 2017

@author: Administrator

问题：如何在线程间进行事件通知
线程间的事件通知，可以使用标准库中Threading.Event:
1)等待事件一端调用wait，等待事件
2)通知事件一端调用set，通知事件
"""

import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from StringIO import StringIO
from Pretty import pretty
from threading import Thread,Event
import tarfile
import os

from Queue import Queue # 使用线程安全的队列

class DownloadThread(Thread):
    """下载线程"""
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance,yahoo.com/table.csv?s=%s.sz'
        self.url %= str(self.sid).rjust(6,'0')
        self.queue = queue
    
    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)
    
    def run(self):
        print 'Download',self.sid
        # 1. download
        data = self.download(self.url)
        # 2. (sid, data)        
        self.queue.append((self.sid,data))

class ConvertThread(Thread):
    """转换线程"""
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent #转换事件
        self.tEvent = tEvent #打包事件
    
    def csvToXml(self, scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = map(lambda h:h.replace(' ',''), headers)
        
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
        pretty(root)
        et = ElementTree(root)
        et.write(fxml)
    
    def run(self):
        """执行线程"""
        count = 0 
        while True:
            sid, data = self.queue.get()
            print 'Convert',sid
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)
                count += 1
                if count == 5:
                    # 达到标准
                   self.cEvent.set()  # 启动打包
                   self.tEvent.wait()
                   self.tEvent.clear()
                   count = 0
                   

class TarThread(Thread):
    """打包线程"""
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent #转换事件
        self.tEvent = tEvent #打包事件
        self.setDaemon(True) # 设置守护线程，其他线程退出以后，本线程自动退出    
    
    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('Data'):
            if fname.endswith('.xml'):
                tf.add('Data/' + fname)
                os.remove('Data/'+ fname)
        tf.close()
        
        if not tf.members:
            os.remove(tfname)
    
    def run(self):
        while True:
            self.cEvent.wait() # 等待转换事件结束
            self.tarXML()
            self.cEvent.clear()
            self.tEvent.set() # 启动转换
            

                    
if __name__=='__main__':
     q = Queue() # 通过队列进行通信
     dThreads = [DownloadThread(i, q) for i in range(1,11)]
     cEvent = Event() # 创建两个事件
     tEvent = Event() 
     cThread = ConvertThread(q, cEvent, tEvent)
     tThread = TarThread(cEvent, tEvent)
     tThread.start()
     
     for t in dThreads:
         t.start()
     cThread.start()
     
     for t in dThreads:
         t.join()
    
     q.put((-1, None))
