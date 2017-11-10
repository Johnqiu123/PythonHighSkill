# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 13:30:22 2017

@author: Administrator

问题:如何使用多线程
使用标准库threading.Thread创建线程，在每一个线程中下载并转换一只股票数据
"""
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from StringIO import StringIO
from Pretty import pretty
from threading import Thread

class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid
    
    def run(self):
        self.handle()
    
    def handle(self):
        print 'Download..(%d)' % self.sid
        url = 'http://table.finance,yahoo.com/table.csv?s=%s.sz'
        url %= str(self.sid).rjust(6,'0')
        rf = download(url)
        if rf is None: return
            
        print 'Convert to xml...(%d)' % self.sid
        fname = str(self.sid).rjust(6, '0') + '.xml'
        with open(fname, 'wb') as wf:
            csvToXml(rf, wf)
def download(url):
    """下载文件"""
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)

def csvToXml(scsv, fxml):
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

if __name__=='__main__':
    threads = []
    for i in range(1, 11):
        t = MyThread(i)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join() # 等待线程执行完
    
    print 'main thread'



