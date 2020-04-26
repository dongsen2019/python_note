# lesson 87 高级模块  shutil

import shutil

# copy 复制文件 把一个文件拷贝到指定的目录中
"""
参数1：要拷贝的文件的路径名
参数2：需要拷贝到别处的路径名，可以重命名
文件不存在则报错：FileNotFoundError: [Errno 2] No such file or directory: '.\\tes.py'
"""
# shutil.copy(".\\test.py", "..\\testagain.py")

# copy2 和 copy方法一样，可以把文件拷贝到指定目录，保留了源文件的信息（操作时间和权限等）

# copyfile 拷贝文件的内容（打开文件，读取内容，写入到新的文件中）
"""
将 src 文件的内容（不含元数据）拷贝到 dst 文件并返回 dst。 src 和 dst 是字符串形式的路径。 dst 必须是完整的目标文件名
"""
# shutil.copyfile(".\\test.py", "..\\testagain.py")  # 如果路径二的文件不存在则新建一个文件

# copytree 可以把整个目录结构和文件全部拷贝到指定目录中，但是要求指定的目录文件夹目录必须不存在
# 否则会报错  FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: '../a'
# shutil.copytree("../practice", "../a")

# rmtree() 删除整个文件夹
# shutil.rmtree("../a")

# move 移动文件或文件夹到指定目录，也可以用于修改文件夹或文件的名称
shutil.move("../a", "../practice")  # 移动
shutil.move("../a", "../practice/abc") # 改名