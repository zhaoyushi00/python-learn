class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        name = f"{self.year} {self.make} {self.model}"
        return name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This is car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # 更新里程表
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles




