from random import randint

class Die:

    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认是六面的"""
        self.num_sides = num_sides

    def roll(self):
        """模拟骰子投掷"""
        return randint(1, self.num_sides)