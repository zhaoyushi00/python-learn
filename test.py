import pandas as pd
import numpy as np

# 读取Excel文件
file_path = 'D:/桌面/散点数据.xlsx'  # 替换为实际文件路径
df = pd.read_excel(file_path)

# 打印原始数据类型
print("原始数据类型：")
print(df.dtypes)

# 打印第三列的前几行数据
print("第三列原始数据：")
print(df.iloc[:, 2].head())

# 处理缺失值和非数值数据，先将所有数据转换为字符串，再尝试转换为浮点型
df.iloc[:, 2] = df.iloc[:, 2].astype(str)
df.iloc[:, 2] = df.iloc[:, 2].str.replace(',', '').astype(float)

# 打印转换后的数据类型
print("转换后的数据类型：")
print(df.dtypes)

# 打印转换后的数据
print("转换后的第三列数据：")
print(df.iloc[:, 2].head())

# 将转换后的数据保存回Excel文件或CSV文件
df.to_excel('D:/桌面/散点数据2.xlsx', index=False)  # 保存为Excel文件
# df.to_csv('/mnt/data/modified_data.csv', index=False)  # 保存为CSV文件
