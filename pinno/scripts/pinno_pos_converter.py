#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import openpyxl

userPos = sys.argv[1]
print('正在打开文件……')

try:
    posFile = open(userPos,mode="r")
    print('打开文件成功！')
    print('load file successfully！')
except:
    print('打开文件失败，请检查文件位置及名称！')
    print('load file fail')
    exit()
print('')

# 读取坐标文件内容
print('正在读取文件……')
print('reading file……')
posContent = posFile.readlines()
posData = []
for x in range(5, len(posContent)-1):
    posData.append(posContent[x].split())

posFile.close()
print('完成文件读取！')
print('End of Reading!')
print('')

# 将数据写入xlsx
print('正在将数据写入xlsx文件……')
print('Writing data to .xlsx……')
wb = openpyxl.Workbook()
sheet = wb.active

sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 10
sheet.column_dimensions['C'].width = 30
sheet.column_dimensions['D'].width = 15
sheet.column_dimensions['E'].width = 15
sheet.column_dimensions['F'].width = 15
sheet.column_dimensions['G'].width = 10

#sheet.merge_cells('A1:K1')
#sheet['A1'] = posContent[2][3:]

sheet['A1'] = 'Designator'
sheet['B1'] = 'Footprint'
sheet['C1'] = 'Comment'
sheet['D1'] = 'Mid X'
sheet['E1'] = 'Mid Y'
sheet['F1'] = 'Rotation'
sheet['G1'] = 'Layer'
sheet['H1'] = 'Ref X'
sheet['I1'] = 'Ref Y'
sheet['J1'] = 'Pad X'
sheet['K1'] = 'Pad Y'

for x in range(len(posData)):
    sheet['A'+str(x+2)] = posData[x][0]
    sheet['B'+str(x+2)] = posData[x][1]
    sheet['C'+str(x+2)] = posData[x][2]
    sheet['D'+str(x+2)] = posData[x][3]
    sheet['E'+str(x+2)] = posData[x][4]
    sheet['F'+str(x+2)] = posData[x][5]
    sheet['G'+str(x+2)] = posData[x][6]

wb.save(userPos[:-4] + '_SMT坐标'+'.xlsx')
wb.close()
print('完成写入并生成xlsx文件！')
print('Successed!！')

exit()
