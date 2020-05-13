# lesson 126 装饰带有多参数的函数

def outer(func):
    def inner(who, name, *args, **kwargs):
        print("约到妹子，聊微信。。。")
        result = func(who, name, *args, **kwargs)
        print("天色已晚，怎么办？")
        return result
    return inner


# 定义多参数的 函数
@outer
def love(who, name, *args, **kwargs):
    print(f"{who}跟{name}畅谈人生。。。")
    print(f"完事了去吃了好多美食", args)
    print("看了一场电影", kwargs)
    return [who, name]

res = love("三多", "思思", "火锅", "辣条", "7块钱的麻辣烫", mov="唐山大地震")
print(res)
"""
love() ==> inner()
    love(...) ==> inner(...)
        inner(...) ==> love(...)
"""
