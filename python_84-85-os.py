# lesson 84 内置模块-系统接口模块-os-1

import os

# os.getcwd() 获取当前的工作目录,注意获取的不是当前脚本的目录，是执行程序时所在的目录
res = os.getcwd()

# 如果在当前目录执行这个脚本文件，那么getcwd获取的就是当前的文件目录
# 如果把执行的目录切换到其他位置，再执行当前脚本，那么获取的就是你执行这个脚本时的目录

# os.chdir() 修改当前的工作目录
os.chdir("E:\pycharm\pythonspace")


# 修改工作目录后，再去获取工作目录
res = os.getcwd()

# os.listdir() 获取当前或指定目录中的所有项(文件、文件夹、隐藏文件)，组成的列表
res = os.listdir()
res = os.listdir(path="E:\pycharm\pythonspace")


# os.mkdir(文件夹路径，权限)    # 创建文件夹
# os.mkdir("aa")  # 默认在工作目录创建一个文件夹
# os.mkdir("E:\pycharm\pythonspace\e\q\o") # 无法递归创建
# os.mkdir("abcd", mode=0o777)    mode需要八进制数
"""
    关于系统中的文件权限，仅限linux系统（多用户并发系统）
    drwxr-xr-x  4 yc  staff     128 11 27 11:40 aa
    dr----x--x  2 yc  staff      64 11 27 11:42 abc
    第一位 d代表是一个目录，如果是-则表示为一个文件
    2-4位：rwx 代表文件所有人(u)的权限
    5-7位：r-x 代表文件所属组(g)的权限
    8-10位：r-x 代表其他人(o)的权限
    
    其中 r w x 代表不同的操作权限  777 分别代表 所有人，所属组，其他人
    r 表示是否可读    4
    w 表示是否可写    2
    x 表示是否可执行  1
"""
# os.mkdir("E:\pycharm/abc/a/b/c") # 不能递归创建

# os.makedirs() 可以递归创建文件夹
# os.makedirs("E:\pycharm/abc/a/b/c")  # 可以递归创建


# lesson 85 内置模块-系统接口模块-os-1

# os.rmdir() 删除 空 文件夹
# os.rmdir("E:\pycharm/abc/a/b/c")  c是一个空的文件夹
# os.rmdir("E:\pycharm/abc/a") # OSError: [WinError 145] 目录不是空的。: 'E:\\pycharm/abc/a'
# 同样文件夹里有文件也是不能使用rmdir()方法删除的

# os.removedirs() 递归删除空文件夹
# os.removedirs("./abc/a/b/c") # 删除路径链条中的从右到左的空文件夹，直到遇到非空文件夹停止，不报错

"""
在mac或linux系统中连续创建了abc目录后又在里面创建a，b，c
此时，使用os.removedirs('./abc/a/b/c')删除时，只删除了c。
为什么？
因为mac系统中的文件夹只要被使用过，都会默认创建一个隐藏文件 .DS_Store，此时这个文件夹不是空文件夹了
"""

# os.remove() 删除文件
# os.remove("./abc/1.txt")

# os.rename() 修改文件或文件夹的名字
# os.rename("./1.txt","./2.txt")

# os.system(path of python's file)
os.system("python test.py")    # 等价于在cmd环境下操作
os.system("dir")




