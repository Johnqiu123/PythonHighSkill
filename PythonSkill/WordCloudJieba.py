# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:29:56 2017

@author: Johqniu
"""
import xlrd
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import jieba
from scipy.misc import imread
import matplotlib.pyplot as plt

d = path.dirname(__file__) # 获取当前文件路径
class WordCloudJieba(WordCloud):
    def __init__(self, isCN = 1, back_coloring_path= None, text_path=None, font_path = None,
                 stopwords_path = None, originimg = None, generateimg = None,
                 background_color = None, max_words = 2000, max_font_size = 100, random_state = 42,
                 width=1000, height=860, margin=2):
        back_coloring = imread(path.join(d, back_coloring_path))  # 设置背景图片
        WordCloud.__init__(self, font_path=font_path,  # 设置字体
               background_color=background_color,  # 背景颜色
               max_words=max_words,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=max_font_size,  # 字体最大值
               random_state=random_state,
               width=width, height=height, margin=margin)
        self.isCN = isCN
        self.text_path = text_path
        self.stopwords_path = stopwords_path
        self.originimg = originimg
        self.generateimg = generateimg
        self.back_coloring =  back_coloring

    # 添加自己的词库分词
    def add_word(self, list):
        for items in list:
            jieba.add_word(items)

    def readExcel(self):
        rbook = xlrd.open_workbook(self.text_path)
        rsheet = rbook.sheet_by_index(2)  # 获取sheet
    
        datastr = ''.join(rsheet.row_values(i)[4] for i in range(1, rsheet.nrows))
        return datastr

    def jiebaclearText(self, text):
        mywordlist = []
        seg_list = jieba.cut(text, cut_all=False)
        liststr = "/ ".join(seg_list)
        f_stop = open(self.stopwords_path)
        try:
            f_stop_text = f_stop.read()
            f_stop_text = unicode(f_stop_text, 'utf-8')
        finally:
            f_stop.close()
        f_stop_seg_list = f_stop_text.split('\n')
        for myword in liststr.split('/'):
            if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
                mywordlist.append(myword)
        return ''.join(mywordlist)

def main():
    # ### 设置参数
    isCN = 1 #默认启用中文分词
    bcpath = "Data/love.jpg" # 设置背景图片路径
    tpath = 'Data/lz.txt' #设置要分析的文本路径
    fpath = 'Data/simkai.ttf' # 为matplotlib设置中文字体路径没
    spath = 'Data/stopwords1893.txt' # 停用词词表
    imgname1 = "Data/WordCloudDefautColors.png" # 保存的图片名字1(只按照背景图片形状)
    imgname2 = "Data/WordCloudColorsByImg.png"# 保存的图片名字2(颜色按照背景图片颜色布局生成)

    wcj =  WordCloudJieba(isCN = isCN, back_coloring_path= bcpath, text_path=tpath, 
                font_path = fpath,stopwords_path = spath, originimg = imgname1, generateimg = imgname2,
                background_color = 'white')
    
    # ### 设置词典
    my_words_list = ['邱龙泉','我爱你','姜玲'] # 在结巴的词库中添加新词
    wcj.add_word(my_words_list)
    
    # ### 打开文本
    text = open(path.join(d, wcj.text_path)).read()
    
    print type(text)
    # ### 中文调用
    if wcj.isCN:
        text = wcj.jiebaclearText(text)
    
    # 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
    wcj.generate(text)
    # wc.generate_from_frequencies(txt_freq)
    # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(wcj.back_coloring)
    
    plt.figure()
    # 以下代码显示图片
    plt.imshow(wcj)
    plt.axis("off")
    plt.show()
    # 绘制词云
    
    # 保存图片
    wcj.to_file(path.join(d, imgname1))
    
    image_colors = ImageColorGenerator(wcj.back_coloring)
    
    plt.imshow(wcj.recolor(color_func=image_colors))
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    plt.imshow(wcj.back_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()
    # 保存图片
    wcj.to_file(path.join(d, imgname2))

def main2():
    # ### 设置参数
    isCN = 1 #默认启用中文分词
    bcpath = "Data/ai.jpg" # 设置背景图片路径
    tpath = 'Data/weixin.xlsx' #设置要分析的文本路径
    fpath = 'Data/simkai.ttf' # 为matplotlib设置中文字体路径没
    spath = 'Data/stopwords1893.txt' # 停用词词表
    imgname1 = "Data/information.png" # 保存的图片名字1(只按照背景图片形状)
    imgname2 = "Data/information2.png"# 保存的图片名字2(颜色按照背景图片颜色布局生成)
    
    tpath = path.join(d, tpath)

    wcj =  WordCloudJieba(isCN = isCN, back_coloring_path= bcpath, text_path=tpath, 
                font_path = fpath,stopwords_path = spath, originimg = imgname1, generateimg = imgname2,
                background_color = 'white')
    
    # ### 设置词典
    my_words_list = ['邱龙泉','我爱你','姜玲'] # 在结巴的词库中添加新词
    wcj.add_word(my_words_list)
    
    # ### 打开文本  
    text = wcj.readExcel()
    text.replace(u"深度学习",u"邱龙泉")
    
    # ### 中文调用
    if wcj.isCN:
        text = wcj.jiebaclearText(text)
    
    # 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
    wcj.generate(text)
    # wc.generate_from_frequencies(txt_freq)
    # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(wcj.back_coloring)
    
    plt.figure()
    # 以下代码显示图片
    plt.imshow(wcj)
    plt.axis("off")
    plt.show()
    # 绘制词云
    
    # 保存图片
    wcj.to_file(path.join(d, imgname1))
    
    image_colors = ImageColorGenerator(wcj.back_coloring)
    
    plt.imshow(wcj.recolor(color_func=image_colors))
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    plt.imshow(wcj.back_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()
    
    # 保存图片
    wcj.to_file(path.join(d, imgname2))    

if __name__=='__main__':
    main2()