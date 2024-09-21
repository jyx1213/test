# 给定的数据点  
data_points = [  
    [0, 0],  
    [0.0004, 13.02764],  
    [0.00101, 28.107465],  
    [0.001501, 41.75075],  
    [0.002601, 56.37815],  
    [0.0077021, 68.83705],  
    [0.025807, 81.924],  
    [0.051212, 96.11395],  
    [0.079517, 106.12075],  
    [0.13203, 114.08885]  
]  
  
# 初始化一个列表来存储斜率  
slopes = []  
  
# 遍历数据点（除了最后一个）来计算斜率  
for i in range(len(data_points) - 1):  
    x1, y1 = data_points[i]  
    x2, y2 = data_points[i + 1]  
    slope = (y2 - y1) / (x2 - x1)  
    slopes.append(slope)  
  
# 打印所有的斜率  
for i, slope in enumerate(slopes):  
    print(f"斜率 {i+1}: {slope:.2f}")
    
  