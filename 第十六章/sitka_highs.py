from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_simple.csv")

# 读取文件 并将文件中的内容进行分行
lines = path.read_text().splitlines()

# 读取文件中的内容
reader = csv.reader(lines)

# 当以reader为参数对象时，函数next返回文件中的下一行
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# print(header_row)

# 获取最高温度
# highs = []
# for row in reader:
#     high = int (row[4])
#     highs.append(high)
# print(highs)

# 提取日期和最高温度
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# plt.style.use('seaborn')
fig, ax = plt.subplots()
# alpha设置透明度,1为完全不透明，0为完全透明
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图表标题和坐标轴标签
ax.set_title("Daily high temperatures, 2021", fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate() # 自动格式化日期
ax.set_ylabel('Temperature (F)', fontsize=16)
# 设置刻度标记的大小
# ax.tick_params(axis='both', which='major', labelsize=16)


plt.show()
