# Gluttonous Snake

"""
Food
Snake
World
"""
import threading
import tkinter
import random
import time
import queue

class Food(): 
    """定义食物，食物包含基本属性和创建食物方法"""
    def __init__(self, queue, scrnwidth, scrnheight):
        # [1] 定义食物的宽度和高度
        self.width = 40
        self.height = 40
        # [2] 定义食物出现的坐标
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        # [3] 存储消息队列
        self.queue = queue
        # [4] 创建食物的坐标
        # self.food_coords = None

    def create_food(self):
        """创建食物"""
        xpos = random.randrange(20, self.scrnwidth - 20, 40)
        ypos = random.randrange(20, self.scrnheight - 20, 40)
        x1 = xpos - self.width / 2
        y1 = ypos - self.height / 2
        x2 = xpos + self.width / 2
        y2 = ypos + self.height / 2

        self.food_coords = (xpos, ypos)
        self.exppos = x1, y1, x2, y2
        self.queue.put({"food": self.exppos})

class Snake(threading.Thread):
    """定义蛇"""
    def __init__(self, gui, queue, canvas, scrnwidth, scrnheight):
        threading.Thread.__init__(self)
        # [1] 贪吃蛇的初始长度
        self.length = 4
        # [2] 蛇的单元尺寸
        self.snakeWidth = 40
        # [3] 赚得的积分
        self.points_earned = 0
        # [4] 存储gui
        self.gui = gui
        # [5] 存储消息队列
        self.queue = queue
        # [6] 存储游戏框的尺寸
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        # [6] 创建食物
        self.food = Food(queue, self.scrnwidth, self.scrnheight)
        self.food.create_food()
        # [7] 蛇尾的位置坐标
        self.xpos = random.randrange(100, scrnwidth - 40 / 2, 40)
        self.ypos = random.randrange(100, scrnheight - 40 / 2, 40)
        # [8] 蛇的运动速度
        self.xvelocity = 40
        self.yvelocity = 40
        # [9] 创建蛇的颜色
        self.color = "#%02x%02x%02x" % (255, 153, 18)
        # [10] 起始的方向
        self.direction = "right"
        # [11] 储存蛇的cell_pos仓库
        self.cell_Cpos = []
        for i in range(self.length):
            self.cell_Cpos.append((self.xpos + i * 40, self.ypos))
        print(self.cell_Cpos)

        # [12] 创建蛇的实体
        self.entity = canvas.create_line((0, 0), (0, 0), fill=self.color, width=self.snakeWidth)

        self.start()

    def keyPress(self, e):
        """根据传递的事件设置方向"""
        self.direction = e.keysym

    def calculate_new_coords(self):
        """根据方向，计算新的运动点位，每次移动属性self.xvelocity,yvelocity"""
        last_x, last_y = self.cell_Cpos[-1]
        new_pos = (last_x + 40, last_y)
        if self.direction == "Up":
            new_pos = (last_x, (last_y - self.yvelocity))
            print(new_pos)
        elif self.direction == "Down":
            new_pos = (last_x, (last_y + self.yvelocity))
        elif self.direction == "Left":
            new_pos = ((last_x - self.xvelocity), last_y)
        elif self.direction == "Right":
            new_pos = ((last_x + self.xvelocity), last_y)
        # 返回新的点位
        return new_pos

    def move(self):
        """根据遇到食物和没有遇到食物两种情况，将蛇的cell_pos仓库更新"""
        new_pos = self.calculate_new_coords()
        if new_pos == self.food.food_coords:
            self.points_earned += 1
            self.cell_Cpos.append(new_pos)
            self.queue.put({"points_earned": self.points_earned})
            self.food.create_food()
        else:
            self.cell_Cpos.pop(0)
            self.check_game_over(new_pos)
            self.cell_Cpos.append(new_pos)

    # 检查是否撞墙
    def check_game_over(self, new_pos):
        """检查游戏是否结束"""
        if (new_pos[0] > self.scrnwidth or new_pos[0] < 0 or
                new_pos[1] > self.scrnheight or new_pos[1] < 0 or new_pos in self.cell_Cpos):
            self.queue.put({"game_over": True})

    # 使蛇运动
    def run(self):
        """多线程，重载run"""
        if self.gui.is_game_over == True:
            del self
        while not self.gui.is_game_over:
            self.queue.put({"move": self.cell_Cpos})
            time.sleep(0.5)
            self.move()

class World():
    """定义游戏世界"""
    def __init__(self):
        # [1] 创建框架
        self.baseFrame = tkinter.Tk()

        # [2] 定义游戏框的尺寸
        self.screenwidth = 1600
        self.screenheight = 1000
        # [3] 创建画布
        self.cvs = tkinter.Canvas(self.baseFrame, width=self.screenwidth, height=self.screenheight)
        "布局画布"
        self.cvs.pack()

        # [4] 消息队列
        self.q = queue.Queue()

        # [5] 游戏是否结束
        self.is_game_over = False

        # [6] 创建蛇和食物对象
        self.snake = Snake(self, self.q, self.cvs, self.screenwidth, self.screenheight)
        self.food = self.cvs.create_rectangle(0, 0, 0, 0, fill="#%02x%02x%02x" % (255, 153, 18),
                                              outline="#%02x%02x%02x" % (255, 153, 18))

        # [5] 创建积分模块
        self.points_earned = self.cvs.create_text(800, 40, fill='blue', text='score:0')

        "消息绑定"
        self.baseFrame.bind("<Key-Up>", self.snake.keyPress)
        self.baseFrame.bind("<Key-Down>", self.snake.keyPress)
        self.baseFrame.bind("<Key-Left>", self.snake.keyPress)
        self.baseFrame.bind("<Key-Right>", self.snake.keyPress)

        self.queue_handler()

        self.baseFrame.mainloop()

    def queue_handler(self):
        """消息队列的消费者，根据不同的任务关键字进行不同的操作"""
        try:
            while True:
                task = self.q.get(block=False)
                print(task)
                if task.get("game_over"):
                    self.game_over()
                elif task.get("points_earned"):
                    self.cvs.itemconfigure(self.points_earned,
                                           text="score:{}".format(task["points_earned"]))
                    self.q.task_done()
                elif task.get("move"):
                    points = [x for point in task["move"] for x in point]
                    self.cvs.coords(self.snake.entity, *points)
                elif task.get("food"):
                    self.cvs.coords(self.food, *task["food"])
        except queue.Empty:
            if self.is_game_over != True:
                self.cvs.after(100, self.queue_handler)

    def game_over(self):
        """当撞墙或者撞到自身，结束游戏，并弹出相应的提示"""
        self.is_game_over = True
        self.cvs.create_text(800, 500, fill="black", text="game over!")
        quitbtn = tkinter.Button(self.baseFrame, text="quit", command=self.baseFrame.destroy)
        rebtn = tkinter.Button(self.baseFrame, text="Begin", command=self.__init__)
        self.cvs.create_window(400, 200, anchor="nw", window=quitbtn)

w = World()





