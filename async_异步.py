class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# 使用示例
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # 输出 True，表示两个实例是同一个对象



