"""
issubclass()函数的使用，判断参数class是不是类型参数的子类
用法：issubclass(class, classinfo)
"""
class A:
    pass
class B(A):
    pass

print(issubclass(B, A))

"""
isinstance()函数的使用，判断一个对象是否是一个已经知道类型的对象
用法: isinstance(object, classinfo)
isinstance()和type()的区别 isinstance会考虑继承关系，type不考虑继承关系
"""
a = 1
print(isinstance(1, int))
print(type(a))