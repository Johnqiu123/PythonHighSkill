# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 22:13:26 2017

@author: Administrator

问题：如何读写excel文件
使用第三方库xlrd和xlwt，这两个库分别用于excel读和写
"""
import xlrd, xlwt

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0) # 获取sheet

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None) # 写入单元格

for row in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1)) # 求和算总分
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyfont('aligh: vertical center, horizontal center')#设置字体的格式

for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('output.xlsx') # 保存新表格
