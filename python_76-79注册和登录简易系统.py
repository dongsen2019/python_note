# lesson 76-79

"""
注册功能
    1.需要用户名和密码以及确认密码
    2.注册时如果用户名已经存在，则不能再次注册
登录功能
    1.需要使用已经注册的用户信息登录
    2.密码输入错误三次后，锁定账户信息（不能再使用这个账户登录）
"""

# 菜单


def menu():
    print("0 注册")
    print("1 登录")
    print("2 退出")


def cfile():
    fp = open("./login.txt", 'w', encoding="utf-8")
    fp.close()
    fp = open("./accountlocked.txt", 'w', encoding="utf-8")
    fp.close()


def isregistered(varstr):   # return bool
    with open("./login.txt", 'r', encoding="utf-8") as fp:
        rusername = fp.readline()
        rusername = rusername[:len(rusername)-1]
        while rusername != varstr and rusername != "":
            rusername = fp.readline()
            rusername = rusername[:len(rusername)-1]
        fp.close()
        if rusername != "":
            return True
        else:
            return False


def islocked(varstr):   # return bool
    with open("./accountlocked.txt", 'r', encoding="utf-8") as fp:
        acclocked = fp.readline()
        acclocked = acclocked[:len(acclocked)-1]
        while acclocked != varstr and acclocked != "":
            acclocked = fp.readline()
            acclocked = acclocked[:len(acclocked) - 1]
        fp.close()
        if acclocked != "":
            return True
        else:
            return False


def signin():
    username = input("请输入用户名：")
    if isregistered(username):
        print("该账号已经注册！")
    else:
        with open("./login.txt", 'a', encoding="utf-8") as fp:
            fp.write(username)
            fp.write('\n')
            fp.close()
        password = ""
        while True:
            password = input("请输入密码：")
            if input("请再次输入密码：") != password:
                print("两次输入的密码不相同，需再次重新输入！")
            else:
                print("注册成功！")
                break
        with open("./login.txt", 'a', encoding="utf-8") as fp:
            fp.write(password)
            fp.write('\n')
            fp.close()


def login():
    times = 2
    username = input("请输入用户名：")
    if islocked(username):
        print("该账户已被锁定！")
    else:
        with open("./login.txt", 'r', encoding="utf-8") as fp:
            rusername = fp.readline()
            rusername = rusername[:len(rusername) - 1]
            while rusername != username and rusername != "":
                rusername = fp.readline()
                rusername = rusername[:len(rusername) - 1]
            if rusername != "":
                password = input("请输入密码：")
                rpassword = fp.readline()
                rpassword = rpassword[:len(rpassword) - 1]
                while times != 0 and password != rpassword:
                    password = input(f"密码错误,还有{times}次输入机会：")
                    times -= 1

                if times != 0:
                    exit("登录成功")
                else:
                    print("3次密码错误，账户锁定")
                    with open("./accountlocked.txt", 'a', encoding="utf-8") as fp:
                        fp.write(username)
                        fp.write('\n')
                        fp.close()
            else:
                print("用户名不存在!")


dic = {0: signin, 1: login}


# main
cfile()
while True:
    menu()
    res = int(input())
    if res < 0 or res > 2:
        print("invalid number,enter again!")
    elif res == 2:
        break
    else:
        dic[res]()
