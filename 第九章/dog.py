class Dog:
    """一次模拟小狗的简单尝试"""
    def __int__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小猴收到命令时坐下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie')