import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()

    # 将所有点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors=None, s=1)
    ax.set_aspect('equal')

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors=None, s=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=10)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    f = input('again? (y/n): ')
    if f == 'n':
        break