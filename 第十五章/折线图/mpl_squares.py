import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
input_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fig, ax = plt.subplots()
ax.plot(input_value, squares, linewidth=3)

# 这只图题 并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(labelsize=14)

plt.show()