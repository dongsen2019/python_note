# lesson 100 日志类的封装

import time

class mylog():
    # 属性成员
    fileurl = "./"
    filename = "log.txt"
    fileobj = None

    # 方法成员
    def __init__(self):
        self.fileobj = open(self.fileurl+self.filename, 'a+', encoding="utf-8")

    def wlog(self, s):
        t = time.strftime("%Y:%m:%d %H:%M:%S")
        self.fileobj.write(t+"  "+s+'\n')

    def __del__(self):
        self.fileobj.close()


l = mylog()
l.wlog("今天是五月二号")
l.wlog("没人陪我出去玩")
l.wlog("只能在家写代码")

