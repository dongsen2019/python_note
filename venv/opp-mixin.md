# OPP-Mixin设计模式
- 主要采用多继承方式对类的功能进行扩展
- [Mixin概念](https://www.zhihu.com/question/20778853)
- [MRO and Mixin](https://blog.csdn.net/robinjwong/article/details/48375833)
- [Mixin模式](https://www.cnblogs.com/xybaby/p/6484262.html)
- [Mixin MRO](http://runforever.github.io/2014-07-19/2014-07-19-python-mixin%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)
- [MRO](http://xiaocong.github.io/blog/2012/06/13/python-mixin-and-mro/)

- 我们使用多继承语法来实现Mixin
- 使用Mixin实现多继承的时候非常小心
    - 首先他必须表示某一单一功能，而不是某个物品
    - 职责必须单一，如果由多个功能，则写多个Mixin
    - Mixin不能依赖于子类的实现
    - 子类即使没有继承Mixin类，也能照样工作，只是缺少了某项功能
- 优点
    - 使用Mixin可以在不对类进行任何修改的情况下，扩充功能
    - 可以方便地组织和维护不同功能组件的划分
    - 可以根据需要任意调整功能类的组合
    - 可以避免创建很多新的类，导致类的继承混乱
   