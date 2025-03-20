class MyClass:
    def my_method(self):
        print("Hello from my_method")


# 动态访问方法
method = MyClass.__dict__['my_method']
method(MyClass())  # 输出: Hello from my_method
