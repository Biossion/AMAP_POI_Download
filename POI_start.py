import requests
import pandas as pd

# API基础URL
base_url = "https://restapi.amap.com/v5/place/text"
# API请求参数
params = {
    "key": "",#填入高德开放平台web服务应用的key
    "types": "150702",#查询的poi兴趣点类型编号
    "region": "320583",#查询的城市区域代码
    "page_num": 1  # 初始页码
}

# 初始化空列表，用于存储所有页的数据
all_pois = []

# 遍历获取每一页的数据
while True:
    # 发送GET请求获取当前页的数据
    response = requests.get(base_url, params=params)
    data = response.json()

    # 检查响应状态
    if data['status'] != "1":
        print("请求失败，错误信息：", data['info'])
        break
    
    # 提取POI数据
    pois = data['pois']
    
    # 如果没有数据，停止循环
    if not pois:
        break
    
    # 将当前页的数据追加到列表中
    all_pois.extend(pois)

    # 输出当前页码及数据数量
    print(f"已获取第 {params['page_num']} 页数据，共 {len(pois)} 条")

    # 增加页码，获取下一页
    params['page_num'] += 1

# 转换为 pandas DataFrame
df = pd.DataFrame(all_pois)

# 保存为 CSV 文件
df.to_csv('poi_data.csv', index=False, encoding='utf-8-sig')

print("所有数据已成功转换并保存为 poi_data.csv 文件。")
