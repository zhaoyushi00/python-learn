import numpy as np
import pandas as pd

# 读取上传的Excel文件
file_path = 'D:/桌面/散点数据.xlsx'  # 替换为实际文件路径
df = pd.read_excel(file_path)

# 打印数据类型
# print("Data types before conversion:")
print(df.dtypes)

# 尝试将所有列转换为数值类型，如果无法转换则填充为NaN
#df = df.apply(pd.to_numeric, errors='coerce')

# 检查并处理缺失值
# print("Checking for missing values:")
# print(df.isnull().sum())

# 填充缺失值或删除包含缺失值的行
#df = df.dropna()  # 删除包含缺失值的行

# 处理缺失值和非数值数据，先将所有数据转换为字符串，再尝试转换为浮点型
# df.iloc[:, 2] = df.iloc[:, 2].astype(str)
# df.iloc[:, 2] = df.iloc[:, 2].str.replace(',', '').astype(float)

# 处理缺失值和非数值数据，先将所有数据转换为字符串，再尝试转换为浮点型
def safe_float_conversion(x):
    try:
        return float(str(x).replace(',', ''))
    except ValueError:
        return np.nan

# 将第三列数据应用安全转换函数
df.iloc[:, 2] = df.iloc[:, 2].apply(safe_float_conversion)

# print("修改后的数据类型：")
print(df.dtypes)

# 将数据转换为numpy数组
demand_points = df.to_numpy()



# 示例需求点坐标及需求量
# 假设已经从图片中提取这些数据
#demand_points = np.array([[104.1637632, 30.6127849382695, 148], [104.1768912, 30.6412115548816, 185], [104.1916704,	30.64460454, 144]])

# 起降场点类型及其覆盖范围和容量
airstrip_types = {
    'type1': {'range': 'l1', 'capacity': 14.6},
    'type2': {'range': 'l2', 'capacity': 17.0},
    'type3': {'range': 'l3', 'capacity': 21.0},
    'type4': {'range': 'ai', 'capacity': 25.0},
    'type5': {'range': 'am', 'capacity': 250.0},
    'type6': {'range': 'an', 'capacity': 500.0},
    'type7': {'range': 'lk', 'capacity': 240.0}
}

# 贪婪算法确定最少起降场点数量
def greedy_airstrip_selection(demand_points, airstrip_types):
    selected_airstrips = []
    uncovered_demand_points = demand_points.copy()

    while uncovered_demand_points.shape[0] > 0:
        best_airstrip = None
        best_coverage = 0

        for airstrip_type, properties in airstrip_types.items():
            for dp in uncovered_demand_points:
                coverage = np.sum(
                    (np.linalg.norm(uncovered_demand_points[:, :2] - dp[:2], axis=1) <= properties['range']) &
                    (uncovered_demand_points[:, 2] <= properties['capacity'])
                )

                if coverage > best_coverage:
                    best_coverage = coverage
                    best_airstrip = (dp[:2], airstrip_type)

        if best_airstrip:
            selected_airstrips.append(best_airstrip)
            covered_indices = np.where(
                (np.linalg.norm(uncovered_demand_points[:, :2] - best_airstrip[0], axis=1) <= airstrip_types[best_airstrip[1]]['range']) &
                (uncovered_demand_points[:, 2] <= airstrip_types[best_airstrip[1]]['capacity'])
            )[0]
            uncovered_demand_points = np.delete(uncovered_demand_points, covered_indices, axis=0)
        else:
            break

    return selected_airstrips

selected_airstrips = greedy_airstrip_selection(demand_points, airstrip_types)
print(selected_airstrips)
