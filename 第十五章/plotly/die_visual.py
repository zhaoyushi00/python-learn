import plotly.express as px
from die import Die

# 创建一个D6
die_1 = Die()
# 创建一个D10，即有十个面的骰子
die_2 = Die(10)

# 只几次骰子并将结构存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1) #随机1到6
# 将随机到的数字进行统计
for value in poss_results:
    frequencies.append(results.count(value))

# 对结果进行可视化
fig = px.bar(x=poss_results, y=frequencies, title='掷两个骰子50000次的结果', labels={'x':'Result', 'y':'Frequency'})

# 指定x轴上刻度标记的间距，再给每个条形都加上标签
fig.update_layout(xaxis_dtick=1)

fig.show()
print(frequencies)
# fig.write_html('die_visual.html')
# fig.write_image('die_visual.png')
fig.write_json('die_visual.json')