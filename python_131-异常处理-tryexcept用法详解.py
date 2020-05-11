# lesson 131 try...except...

# 1.使用try...except 处理指定的异常。如果引发了非指定的异常，则无法处理
try:
    s1 = "hello"
    int(s1) # 会引 ValueError
except ValueError as e:
# except IndexError as e:  #如果引发了非指定的异常，则无法处理
    print(e)

# 2.多分支处理异常类
try:
    s1 = "hello"
    # int(s1)    # ValueError
    s1[5]        # IndexError
except IndexError as e:
    print("IndexError", e)
except KeyError as e:
    print("KeyError", e)
except ValueError as e:
    print("ValueError", e)

# 3.通用异常类 Exception
s1 = "world"
try:
    int(s1)
except Exception as e:
    print("Exception ==", e)  # Exception == invalid literal for int() with base 10: 'world'

# 4.多分支异常类+通用异常类，这样引发异常后会按照从上往下的顺序去执行对应的异常处理类
try:
    s1 = "hello"
    # int(s1)    # ValueError
    s1[5]        # IndexError
except IndexError as e:
    print("IndexError", e)
except KeyError as e:
    print("KeyError", e)
except ValueError as e:
    print("ValueError", e)


# 5.try...except...else...
try:
    s1 = "hello"
    # int(s1)    # ValueError
    s1[2]        # IndexError
except IndexError as e:
    print("IndexError", e)
except KeyError as e:
    print("KeyError", e)
except ValueError as e:
    print("ValueError", e)
else:
    print("try代码块中没有引发异常时，执行")

# 6.try...except...else...finally
# finally 无论是否引发异常，都会执行，通常情况下用于执行一些清理工作
try:
    s1 = "hello"
    int(s1)    # ValueError
except IndexError as e:
    print("IndexError", e)
except KeyError as e:
    print("KeyError", e)
except ValueError as e:
    print("ValueError", e)
else:
    print("try代码块中没有引发异常时，执行")
finally:
    print("无论是否引发了异常，都会执行这个代码块")

print("如果上面的代码有异常并且进行了处理，那么后面的代码将继续执行")

# 7.使用raise，主动抛出异常
try:
    # 可以使用 raise 主动抛出异常，并且设置异常信息
    raise Exception('a')
except Exception as e:
    print("Exception", e)

# 8.断言语句
assert 1 == 1  # 如果表达式正确，则什么都不做
assert 2 == 1  # 如果后面的表达式错误，则直接抛出 AssertionError

