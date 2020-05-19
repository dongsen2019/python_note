

"""
虚拟环境
虚拟环境就是在当前的系统环境中，去配置另外一个python的运行环境，是可以创建多个不同的虚拟环境。

python的虚拟环境相互独立，互不影响。

虚拟环境中可以在没有权限的情况下安装新的库（Linux系统中可能会出现的问题）
不同的应用可以使用不同的库或不同的版本。
虚拟环境中的库升级也不影响其它环境
虚拟环境可以作为一个项目的专有环境。在需要部署时，一键导出项目的所需要的包
如何去使用python的虚拟环境
1。在pycharm中可以直接创建虚拟环境

2。自己安装独立的虚拟环境
创建虚拟环境
进入虚拟环境，激活虚拟环境
linux
# 使用 source 命令 去执行 v1/bin/ 目录下的 activate
localhost:code yc$ source v1/bin/activate
(v1) localhost:code yc$
windows
# windows系统需要 进入 v1/Scripts/ 这个目录
cd v1/Scripts/
# 运行 activate.bat 文件
activate.bat
(v1) F:\code>
接下来就可以在虚拟环境中安装一些包
查看是否安装了某个包

退出虚拟环境
linux : deactivate
Windows： 直接ctrl+c
导出当前环境中所有安装过的包
删除环境
python -m venv 虚拟环境名

pip install pymysql

pip show pymysql 如果安装过则能显示信息。

# 查看所有安装的包
pip list
'''
Package      Version
------------ -------
Click        7.0
Flask        1.1.1
itsdangerous 1.1.0
Jinja2       2.10.3
MarkupSafe   1.1.1
pip          19.0.3
PyMySQL      0.9.3
setuptools   40.8.0
Werkzeug     0.16.0
'''

# 导出所有包到文件
pip freeze > ./requirements.txt
退出虚拟环境后，直接删除虚拟环境文件夹即可
"""