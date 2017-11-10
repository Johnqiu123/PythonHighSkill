# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 13:27:36 2017

@author: Administrator

问题：如何线程间通信
使用标准库中Queue.Queue，它是一个线程安全的队列
Download线程把下载数据放入队列，Convert线程从队列里提取数据
"""
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from StringIO import StringIO
from Pretty import pretty
from threading import Thread

from Queue import Queue # 使用线程安全的队列

class DownloadThread(Thread):
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
    def __init__(self):
        Thread.__init__(self)
    
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
        while True:
            sid, data = self.queue.get()
            print 'Convert',sid
            if sid == -1:
                 break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)
                    
if __name__=='__main__':
     q = Queue() # 通过队列进行通信
     dThreads = [DownloadThread(i, q) for i in range(1,11)]
     cThread = ConvertThread(q)
     for t in dThreads:
         t.start()
     cThread.start()
     
     for t in dThreads:
         t.join()
    
     q.put((-1, None))
       
