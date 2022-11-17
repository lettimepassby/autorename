import os
import pandas as pd
import win32api,win32con

allFile = os.listdir('./')
for fn in allFile:
    fnLast = os.path.splitext(fn)[1]  # 分割，不带后缀名
    if(fnLast == '.xlsx'):
        srocFileName = fn
data = pd.read_excel('./'+srocFileName)
datalist = os.listdir('img/')
cont = 0
for i in datalist:
    # 取文件用户名
    fileUserName = i.split('-')[1]
    # 取文件后缀
    fileLast = os.path.splitext(i)[1] # 分割，不带后缀名
    # 查找对应数据
    dataUserName = data[(data['提交者（自动）'] == fileUserName)]
    # 定义文件名
    fileName = dataUserName.iloc[0].at['姓名（必填）'] + str(dataUserName.iloc[0].at['学号（必填）'])
    # 重命名
    os.rename('img/'+i, 'img/'+fileName.strip()+fileLast)
    cont += 1

win32api.MessageBox(0, '图片重命名已完成', '时流TimePassBy',win32con.MB_OK)
