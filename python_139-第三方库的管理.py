# lesson 139 第三方库的管理

"""
python中比较牛逼的地方就是由大量的第三方库提供给你使用

第三方库的管理网站http://pypi.org/

如何安装第三方库
pip
    pip就是python的包管理工具，解决了包直接的依赖关系。可以方便的管理第三方库（包）
    类似于PHP中Composer，或者Nodejs中的npm，或者Linux中的yum。

如何使用pip
    pip install 包名（库名）
    注意：如果有多个python环境的情况下，可能需要使用pip3

更换pip的镜像源
pip国内的一些镜像

  阿里云 http://mirrors.aliyun.com/pypi/simple/ 
  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
  豆瓣(douban) http://pypi.douban.com/simple/ 
  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

修改源方法：

临时使用： 
可以在使用pip的时候在后面加上-i参数，指定pip源 
eg: pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple

永久修改： 
linux: 
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
1
2
windows: 

直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，在pip 目录下新建文件pip.ini，内容如下

或者按照网友的建议：win+R 打开用户目录%HOMEPATH%，在此目录下创建 pip 文件夹，在 pip 目录下创建 pip.ini 文件, 内容如下

[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
"""