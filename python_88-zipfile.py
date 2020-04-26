# lesson 88 压缩模块 zipfile

import zipfile

"""
zipfile.ZipFile(路径包名，模式，压缩方式)
"""

# with zipfile.ZipFile("..//spam.zip", 'w') as myzip:
#     myzip.write("E:/pycharm/practice/python_1-10.py")
#     myzip.write("E:/pycharm/practice/test.py")

# 解压缩后的文件夹包的路径名为压缩时的路径名
# with zipfile.ZipFile("../spam.zip", 'r') as myzip:
#     myzip.extractall("../a")

import os

# 不同的压缩方式，压缩文件的大小差距很大
"""
zipfile.ZIP_STORED
未被压缩的归档成员的数字常数。

zipfile.ZIP_DEFLATED
常用的 ZIP 压缩方法的数字常数。需要 zlib 模块。

zipfile.ZIP_BZIP2
BZIP2 压缩方法的数字常数。需要 bz2 模块。

3.3 新版功能.

zipfile.ZIP_LZMA
LZMA 压缩方法的数字常数。需要 lzma 模块。
"""
# with zipfile.ZipFile("..//spam2.zip", 'w') as myzip:
#     res = os.listdir("../practice")
#     for i in res:
#         myzip.write(i)

with zipfile.ZipFile("..//spam2.zip", 'w', zipfile.ZIP_LZMA) as myzip:
    res = os.listdir("../practice")
    for i in res:
        myzip.write(i)

import  shutil

# 使用 shutil.make_archive() 这个方法压缩文件比zip更方便
"""
参数1 创建压缩文件名称
参数2 指定的压缩格式 zip or tar
参数3 要压缩的文件或文件路径
"""


shutil.make_archive("../spam3", "zip", "../practice")