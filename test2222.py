"""
Munch方法，可以改变字典的访问方式
"""
import base64

# from munch impot Munch
# dict1=Munch({'a': 1, 'b': 2, 'c': {'1': 3, '2': 4}, 'd': {'5': {'2': 5, '3': 6}, '4': {'1': 7}}})
# # dict2 = Munch(dict1)
# print(dict1.c)
"""
时间戳转换为标准时间格式
"""
# import time
# now = int(time.time())
# timearry = time.localtime(now)   # 查看当前时间的属性值
# timetran = time.strftime('%Y-%m-%d', timearry)
# print(timetran)

"""
类（对象）的初始化方法：__init__ 的用法。
"""
# class Dog(object):
#     # 定义init方法，并且定义了对象的三个属性
#     def __init__(self, _name, _age, _color):
#         self.name = _name
#         self.age = _age
#         self.color = _color
#
#     def juju(self, _name, _age, _color):
#         self.name = _name
#         self.age = _age
#         self.color = _color
#
# # 创建一个obj对象
# cat = Dog('juju', '18', 'white')
#
# # 格式化打印对象属性
# print(f'我养了一只小猫咪，她的名字叫{cat.name},今年已经{cat.age}岁了，她有非常好看的毛发，是{cat.color}的，朋友都说她是有种西域美人的风范，而且她还非常的乖巧！')
"""字典的使用"""
# obj = {
#     "name": 'jack',
#     "age": '23',
# }
# arr = ['1', '2', '2']
#
# a = obj["name1"]
# print(a)
"""
将正常时间转换成13位的时间戳
"""
# import time
# timestamp = int(time.time() * 1000)
# print(timestamp)
"""
is 和 ==的区别
"""
# a = 555
# b = 555
# print(a == b)
# print(a is b)
"""
base64.encodebytes(s) 方法的使用。可以使用base64编码的数据将字符串编码为二进制形式
"""
# import base64
# s = b'hello world!'
# s1 = base64.encodebytes(s)
# print(s1)
"""
字典的删除、修改、添加
"""
# scores = {
#       '林黛玉': 95,
#       '薛宝钗': 93,
#       '贾宝玉': 78,
# }
#
# scores['林黛玉'] = 90
# print(scores)
# # 输出：{'林黛玉': 90, '薛宝钗': 93, '贾宝玉': 78}
#
# # 添加
# scores['袭人'] = 85
# print(scores)
# # 输出：{'林黛玉': 90, '薛宝钗': 93, '贾宝玉': 78, '袭人': 85}
#
# # 删除
# del scores['林黛玉']
# print(scores)
# # 输出：{'薛宝钗': 93, '贾宝玉': 78, '袭人': 85}

