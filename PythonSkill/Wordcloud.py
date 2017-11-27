# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:13:02 2017

@author: Administrator
"""
from wordcloud import WordCloud
import requests
from StringIO import StringIO
import os

def download(url):
    """下载文件"""
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)
        
if __name__=='__main__':
    
    # Download text
#    url = 'http://labfile.oss.aliyuncs.com/courses/756/constitution.txt'
#    rf = download(url)
#    print(type(rf))
    
    # write text
    fname = 'Data/constitution.txt'
#    with open(fname, 'w') as fw:
#        fw.write(rf.read())
    
    # Read the whole text
    text = open(fname).read()
    
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)
    
#    print wordcloud.__setattr__
#    print os.path.dirname(__file__)
#    path = os.path.join(os.path.dirname(__file__), 'stopwords')
#    print path
    
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    
    # lower max_font_size
#    wordcloud = WordCloud(max_font_size=40).generate(text)
#    plt.figure()
#    plt.imshow(wordcloud)
#    plt.axis("off")
#    plt.show()