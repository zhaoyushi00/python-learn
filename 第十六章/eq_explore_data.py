from pathlib import Path
import plotly.express as px
import pandas as pd
import json

# 将数据作为字符栓读取并转换为python对象
path = Path('eq_data/eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except :
    contents = path.read_text(encoding='utf-8')
# 转python对象
all_eq_data = json.loads(contents)

# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
# print(all_eq_dicts[0])

# 提取震级和位置信息
mags, tittle, lons, lats = [], [], [], []
for mag in all_eq_dicts:
    mags.append(mag['properties']['mag'])
    tittle.append(mag['properties']['title'])
    lons.append(mag['geometry']['coordinates'][0])
    lats.append(mag['geometry']['coordinates'][1])

# path = Path('eq_data/readable_eq_data.geojson')
# #将python对象转换为json格式
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

data = pd.DataFrame(
    data = zip(lons, lats, tittle, mags),
    columns=['经度','纬度','位置','震级']
)
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',

    range_x=(-200,200),
    range_y=(-90,90),
    width=800,
    height=800,
    title='全球地震散点图',
    # 设置散点大小
    size='震级',
    size_max=10,
    # 设置散点颜色
    color='震级',
    #位置
    hover_name='位置'
)
fig.show()
fig.write_html('my_global_earthquake.html')