import tkinter

# 初始化
tk = tkinter.Tk()

# 定义计算器尺寸
tk.geometry("250x380")
tk.title("计算器")

# 定义显示标签外框
frame_show = tkinter.Frame(tk, width=300, height=150, bg="#dddddd")
frame_show.pack()

# 显示框的字符串变量
sv = tkinter.StringVar()
sv.set('0')

# 定义显示标签
show_label = tkinter.Label(frame_show, textvariable=sv, width=12, height=1, bg="green",
                           font=("黑体", 20, "bold"), justify="left", anchor='e')
show_label.pack(padx=10, pady=10)

# 定义键盘框架
frame_bord = tkinter.Frame(tk, width=300, height=450, bg="#cccccc")

# 声明操作数和操作符

"用于存储显示字符串"
num1 = ''
num2 = ''
operator = ''


# 按键后屏显变更
def change(arg):
    global num1, num2
    # 当参数是操作符时：
    if arg in ['+', '-', '*', '/']:
        num2 = num2 + arg
        sv.set(num1 + num2)
        num1 = num1 + num2
        num2 = ''
    # 当操作符为空时
    elif not bool(operator):
        num1 = num1 + arg
        sv.set(num1)
    else:
        num2 = num2 + arg
        sv.set(num1 + num2)
        num1 = num1 + num2
        num2 = ''


# 按操作符键
def operation(op):
    global operator, num1
    if op in ['+', '-', '*', '/']:
        operator = op
        change(op)
    else:
        res = eval(num1)
        sv.set(str(res))
        num1 = str(res)

# 定义delete
def delete():
    pass

# 定义clear
def clear():
    global num1, num2, operator
    num1 = ''
    num2 = ''
    operator = ''
    sv.set('0')

# 定义取相反数
def fan():
    pass

# 定义ce


# 定义键盘按键
button_del = tkinter.Button(frame_bord, text='←', width=5, height=1,
                            command=delete).grid(row=0, column=0)
button_clear = tkinter.Button(frame_bord, text='C', width=5, height=1,
                              command=clear).grid(row=0, column=1)
button_fan = tkinter.Button(frame_bord, text='±', width=5, height=1,
                            command=fan).grid(row=0, column=2)
button_ce = tkinter.Button(frame_bord, text='ce', width=5, height=1,
                           command=clear).grid(row=0, column=3)
button_1 = tkinter.Button(frame_bord, text='1', width=5, height=1,
                          command=lambda: change('1')).grid(row=1, column=0)
button_2 = tkinter.Button(frame_bord, text='2', width=5, height=1,
                          command=lambda: change('2')).grid(row=1, column=1)
button_3 = tkinter.Button(frame_bord, text='3', width=5, height=1,
                          command=lambda: change('3')).grid(row=1, column=2)
button_add = tkinter.Button(frame_bord, text='+', width=5, height=1,
                            command=lambda: operation('+')).grid(row=1, column=3)
button_4 = tkinter.Button(frame_bord, text='4', width=5, height=1,
                          command=lambda: change('4')).grid(row=2, column=0)
button_5 = tkinter.Button(frame_bord, text='5', width=5, height=1,
                          command=lambda: change('5')).grid(row=2, column=1)
button_6 = tkinter.Button(frame_bord, text='6', width=5, height=1,
                          command=lambda: change('6')).grid(row=2, column=2)
button_minus = tkinter.Button(frame_bord, text='-', width=5, height=1,
                              command=lambda: operation('-')).grid(row=2, column=3)
button_7 = tkinter.Button(frame_bord, text='7', width=5, height=1,
                          command=lambda: change('7')).grid(row=3, column=0)
button_8 = tkinter.Button(frame_bord, text='8', width=5, height=1,
                          command=lambda: change('8')).grid(row=3, column=1)
button_9 = tkinter.Button(frame_bord, text='9', width=5, height=1,
                          command=lambda: change('9')).grid(row=3, column=2)
button_multiply = tkinter.Button(frame_bord, text='*', width=5, height=1,
                                 command=lambda: operation('*')).grid(row=3, column=3)
button_0 = tkinter.Button(frame_bord, text='0', width=5, height=1,
                          command=lambda: change('0')).grid(row=4, column=0)
button_dot = tkinter.Button(frame_bord, text='.', width=5, height=1,
                            command=lambda: change('.')).grid(row=4, column=1)
button_divide = tkinter.Button(frame_bord, text='/', width=5, height=1,
                               command=lambda: operation('/')).grid(row=4, column=2)
button_eq = tkinter.Button(frame_bord, text='=', width=5, height=1,
                           command=lambda: operation('=')).grid(row=4, column=3)

frame_bord.pack(padx=10, pady=10)

tk.mainloop()
