import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.font_manager import FontProperties  # 导入FontProperties
my_font = FontProperties(fname="C:\Windows\Fonts\simkai.ttf", size=14)  # 设置字体

#原始训练数据
read_csv1 = pd.read_csv(r"C:\Users\14380\Desktop\Data Mining Projects\原始数据.csv")
print(read_csv1)


#第二个表透视
pivot_table_predict3 = read_csv1.pivot_table(index=['first_cate_code','second_cate_code'],values=['ord_qty'],aggfunc=sum)
print(pivot_table_predict3)

#第三个透视表(根据季度来划分)
pivot_table_predict4 = read_csv1.pivot_table(index=['order_date','first_cate_code','second_cate_code'],values=['ord_qty'],aggfunc=sum)
print(pivot_table_predict4)
pivot_table_predict4.to_csv('时间-销售总量.csv')


#单个价格表
price_total_graph = read_csv1.assign(price_total=lambda x: x.item_price*x.ord_qty)
price_total_graph.to_csv("总花费量.csv")
print(price_total_graph)
print(price_total_graph.describe())
print(price_total_graph.info())

#画图类
#第一问画图
price_total_graph_delete_error = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\异常值处理2.csv')
x = price_total_graph_delete_error['1005']
y = price_total_graph_delete_error['11']
plt.scatter(x,y)
plt.xlabel('Price')
plt.ylabel('Order amount')
plt.title('Price-Needs')
cov = np.cov(x,y)
plt.grid()
#print(cov)
plt.show()

#根据销售区域代码随着代码的增加
pivot_table_region = read_csv1.pivot_table(index=['sales_region_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_region)
plt.bar(x=pivot_table_region.index,height=pivot_table_region['ord_qty'])
plt.xlabel('Regions')
plt.ylabel('Order amount')
plt.title('Region-Needs')
plt.grid()
plt.show()

#根据大类发现产品大类指标，随着该代码的增加，其需求越高
pivot_table_class = read_csv1.pivot_table(index=['first_cate_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_class)
plt.bar(x=pivot_table_class.index,height=pivot_table_class['ord_qty'])
plt.xlabel('First Class')
plt.ylabel('Order Amount')
plt.title('First Class-Needs')
plt.grid()
plt.show()

#线下线上售卖情况
pivot_table_sales_chan = read_csv1.pivot_table(index=['sales_chan_name'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_sales_chan)
plt.bar(x=pivot_table_sales_chan.index,height=pivot_table_sales_chan['ord_qty'])
plt.xlabel('Order Type')
plt.ylabel('Order Amount')
plt.title('Order Type-Needs')
plt.grid()
plt.show()

#细类画图
pivot_table_sales_second_cate = read_csv1.pivot_table(index=['second_cate_code'],values=['ord_qty'],aggfunc=sum)
print(pivot_table_sales_second_cate)
plt.bar(x=pivot_table_sales_second_cate.index,height=pivot_table_sales_second_cate['ord_qty'])
plt.title('Second Class-Needs')
plt.xlabel('Second Class')
plt.ylabel('Order Amount')
x = range(401,413,1)
plt.xticks(x)
plt.grid()
plt.show()




























