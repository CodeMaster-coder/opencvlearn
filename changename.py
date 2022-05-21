# *_* coding : UTF-8 *_*
# 开发人员   ：csu·pan-_-||
# 开发时间   ：2020/11/22 11:45
# 文件名称   ：renameFile.py
# 开发工具   ：PyCharm
# 功能描述   ：将一个文件夹下的所有文件重命名

import os
path = 'D:\\visiondetect\\new'
files = os.listdir(path)  # 文件夹里的所有文件名存成列表list
for i, file in enumerate(files):
    # 重点在05d，这样会自动补齐5位，不足的补零
    # 为啥是0 + i，方便后面添加，把0改了就行
    NewFileName = os.path.join(path, 'neg-' + '%d'%(i+1) +'.jpg')
    OldFileName = os.path.join(path, file)
    # print('第%d个文件：%s'%(i+1,newName))
    os.rename(OldFileName, NewFileName)  # 改名
