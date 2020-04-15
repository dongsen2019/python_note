# lesson 72
# Python中的File(文件)操作

# 文件操作步骤
"""
1.打开文件 2.读写文件 3.关闭文件
"""

# 文件操作的相关函数

"""
1.打开文件 open()
    参数1：文件路径
        路径 url 统一资源定位符
        相对路径：
            针对文件的相对路径的表示，从当前目录开始计算
                ./1.txt ==>  ./ 代表当前目录开始计算
                ../1.txt ==> ../ 代表当前目录中的 上一级目录中的1.txt
                ../a/b/c/1.txt  代表上一级目录中的a/b/c/1/txt
        绝对路径：
                windows:    c:/users/appdata/1.txt
                Linux:      /user/home/yc/1.txt
    参数2：打开的方式
        基础模式： w r x a
        w 模式 write 写入
            1.文件如果不存在，则创建这个文件
            2.文件如果存在，则打开这个文件，并且清空文件内容
            3.文件打开后，文件的指针在文件的最前面
        r 模式：read 读取模式
            1.如果文件不存在，则报错
            2.文件如果存在，则打开文件
            3.文件指针在文件的最前面
        x 模式：xor 异或模式
            1.文件不存在，则创建这个文件
            2.文件已存在，则报错(防止覆盖)
            3.文件的指针在文件的最前面 
        a 模式：append 追加模式
            1.文件不存在，则创建文件
            2.如果文件存在，则打开文件
            3.文件指针在文件的最后
            
        扩展模式：
            b 模式 bytes 二进制
            + plus模式   增强模式(可读可写)
        
        文件操作模式的组合：
            w,r,a,x
            wb,rb,ab,xb
            w+,r+,a+,x+
            wb+,rb+,ab+,xb+  
        
    参数 encoding 可选参数，设置文件的字符集
        如果是一个二进制的文件时，不需要设置字符集
        一般 encoding='utf-8' 或者不写
"""

fp = open("./1.txt", 'w', encoding="utf-8")
print(fp,type(fp))

# 2.写入
# 使用文件对象，调用 write() 方法 写入内容
fp.write("hello world!")


# 3.关闭文件
# 使用文件对象 调用close() 方法 关闭文件
fp.close()


# lesson 73
# 文件的打开模式


# lesson 74
# 打开模式的演示操作

# 追加模式

# 1.打开文件
fp = open("./1.txt", 'a', encoding="utf-8")
# 2.写入/读取 文件
fp.write("\nhow are you！")
# 3.关闭文件
fp.close()

# 读取操作

# 1.打开文件
fp = open("./1.txt", 'r', encoding="utf-8")

# 2.读取文件
varstr = fp.read()
print(varstr)

# 3.关闭文件
fp.close()

# 文件操作的 高级写法

"""
with open(文件路径，打开模式)
    变量.方法()
"""

# 好处是不用写关闭
# 注意：使用 w+ 虽然可读可写，但是打开文件时会清空文件
# a+ 追加写，并且可读，但由于打开文件时光标在最后，无法读到任何内容
# x+ 异或


with open("./1.txt", 'r+', encoding="utf-8") as fp:
    fp.write("\ndongsen")

with open("./1.txt", 'a+', encoding="utf-8") as fp:
    fp.write("\ndongsen")
    fp.seek(0)
    res = fp.read()
    print(res)


# lesson 75
# 文件操作的相关函数

# 写入相关函数

varstr = 5211 # write() argument must be str, not int
with open("./2.txt", 'w', encoding="utf-8") as fp:
    fp.write(varstr)  # write()只能写入str类型的数据
    fp.writelines(varstr)  # 可以写入容器类型数据，注意容器中的元素也必须是字符串


# 读取相关函数
with open("./2.txt", 'r', encoding="utf-8") as fp:
    res = fp.read()  # 默认从当前指针位置读取
    res = fp.read(3) # 设置读取字节的长度
    res = fp.readline() # 读取一行
    res = fp.readlines() # 一次读取多行数据，每行作为一个元素


with open("./2.txt", 'r+', encoding="utf-8") as fp:
    # a+模式，指针默认在文件内容的最后，所以直接读是读取不到内容的
    fp.seek(0) # 把文件指针设置到文件开头位置
    fp.seek(10) # 设置指针的位置为10
    fp.seek(0,2)  # 0,2是文件指针设置在结尾
    # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
    #         0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。


# truncate() 截取文件内容
with open("./1.txt", 'r+', encoding="utf-8") as fp:
    res = fp.truncate(5)
    # 默认从文件的首行的首个字符开始进行截断，截断的长度为size个字符数，
    # size如果为0，则从当前位置截断到最后

print(res)
