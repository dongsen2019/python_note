# 屏保

"""
TKinter项目实战-屏保
项目分析
屏保可以自己启动，也可以手动启动
一旦敲击键盘或者移动鼠标后，或者其他的引发时间，则停止
如果屏保是一幅画的话，则没有画框
图像的动作是随机的，具有随机性，可能包括颜色，大小，多少， 运动方向，变形等
整个世界的构成是：
ScreenSaver:
需要一个canvas， 大小与屏幕一致，没有边框
Ball
颜色，大小，多少， 运动方向，变形等随机
球能动，可以被调用
"""

import random
# from tkinter import *
import tkinter


class random_ball():
    def __init__(self, canvas, scrnwide, scrnheight):
        # [1.球的起始点的x,y坐标]
        self.xpos = random.randint(10, scrnwide-20)
        self.ypos = random.randint(10, scrnheight-20)
        # [2.球的x,y方向的速度]
        self.xvelocity = random.randint(4, 12)
        self.yvelocity = random.randint(4, 12)
        # [3.球的半径R]
        self.radius = random.randint(30, 120)
        # [4.球的颜色]
        c = lambda: random.randint(0, 255)
        self.color = "#%02x%02x%02x"%(c(), c(), c())
        # [5.存储屏幕的尺寸大小]
        self.scrnwide = scrnwide
        self.scrnheight = scrnheight
        # [6.存储画布对象]
        self.cvs = canvas

        "计算球的左上角坐标和右下角坐标，以备绘制球时使用"
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        # [5.绘制球]
        self.entity = canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 撞墙设置
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        if self.xvelocity > 0 and self.xpos + self.radius > self.scrnwide:
            self.xvelocity *= -1
        elif self.xvelocity < 0 and self.xpos - self.radius < 0:
            self.xvelocity *= -1

        if self.yvelocity > 0 and self.ypos + self.radius > self.scrnheight:
            self.yvelocity *= -1
        elif self.yvelocity < 0 and self.ypos - self.radius < 0:
            self.yvelocity *= -1

        # 在画布上移动球
        self.cvs.move(self.entity, self.xvelocity, self.yvelocity)


class ScreenSaver():
    def __init__(self):
        # [1.定义框架]
        self.baseFrame = tkinter.Tk()

        "取消边框"
        self.baseFrame.overrideredirect(1)

        "消息绑定"
        self.baseFrame.bind('<Motion>', self.myquit)

        "获取屏幕的尺寸"
        w = self.baseFrame.winfo_screenwidth()
        h = self.baseFrame.winfo_screenheight()

        # [2.定义画布]
        self.cvs = tkinter.Canvas(self.baseFrame, width=w, height=h)

        "画布布局"
        self.cvs.pack()
        self.cvs.update()

        # [3.指定球的随机数]
        self.ball_num = random.randint(12, 18)
        # [4.创建存储球的仓库]
        self.ball_list = []

        "将创建的球的实体放入仓库"
        for i in range(self.ball_num):
            self.ball_list.append(random_ball(self.cvs, w, h))

        self.run_screen_saver()
        self.baseFrame.mainloop()

    def run_screen_saver(self):
        for b in self.ball_list:
            b.move_ball()

        self.cvs.after(20, self.run_screen_saver)

    def myquit(self, e):
        # 摧毁框架
        self.baseFrame.destroy()


if __name__ == "__main__":
    ScreenSaver()













