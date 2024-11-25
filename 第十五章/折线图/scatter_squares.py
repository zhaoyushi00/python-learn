import matplotlib.pyplot as plt

x_value = range(1,1001)
# 列表推导式
y_value = [x**2 for x in x_value]

# 图形背景版式
plt.style.use('seaborn-v0_8')

# fig表示整个图形 ax表示新绘制的图形
fig, ax = plt.subplots()

# scatter表示绘制散点图，s表示点的大小
# 参数c类似于color，表示颜色映射，cmap表示颜色映射表，颜色首字母大写
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)

# 这只图题 并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#设置坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 覆盖默认的刻度标记样式,即不使用科学计数法
# ax.ticklabel_format(style = 'plain')

# 设置刻度标记的大小
ax.tick_params(labelsize=14)

# 保存图形
plt.savefig('zhaoysuhi.png', bbox_inches='tight')

#显示图片
plt.show()