import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

from matplotlib.font_manager import FontProperties  # 导入FontProperties
my_font = FontProperties(fname="C:\Windows\Fonts\simkai.ttf", size=14)  # 设置字体

#原始训练数据
read_csv1 = pd.read_csv(r"C:\Users\14380\Desktop\Data Mining Projects\原始数据.csv")
print(read_csv1)


#print(pivot_table_predict)
#print(pivot_table_predict2)
#x = pivot_table_predict2['item_code']
#plt.plot(pivot_table_predict2)
#plt.show()


#pivot_table_order_train = read_csv1.pivot_table(index=[])
#print(sum(pivot_table_predict['item_code']))

#第二个表透视
pivot_table_predict3 = read_csv1.pivot_table(index=['first_cate_code','second_cate_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_predict3)

#第三个透视表(根据季度来划分)
pivot_table_predict4 = read_csv1.pivot_table(index=['order_date','first_cate_code','second_cate_code'],values=['ord_qty'],aggfunc=sum)
print(pivot_table_predict4)
pivot_table_predict4.to_csv('时间-销售总量.csv')


#单个价格表
price_total_graph = read_csv1.assign(price_total=lambda x: x.item_price*x.ord_qty)
price_total_graph.to_csv("总花费量.csv")
#print(price_total_graph)
#print(price_total_graph.describe())
#print(price_total_graph.info())


#画图类
#第一问画图
x = price_total_graph['item_price']
y = price_total_graph['ord_qty']
plt.scatter(x,y)
plt.xlabel('Price')
plt.ylabel('Order amount')
plt.title('Price-Needs')
cov = np.cov(x,y)
#print(cov)
plt.show()

#根据销售区域代码随着代码的增加
pivot_table_region = read_csv1.pivot_table(index=['sales_region_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_region)
plt.bar(x=pivot_table_region.index,height=pivot_table_region['ord_qty'])
plt.xlabel('Regions')
plt.ylabel('Order amount')
plt.title('Region-Needs')
plt.show()

#根据大类发现产品大类指标，随着该代码的增加，其需求越高
pivot_table_class = read_csv1.pivot_table(index=['first_cate_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_class)
plt.bar(x=pivot_table_class.index,height=pivot_table_class['ord_qty'])
plt.xlabel('First Class')
plt.ylabel('Order Amount')
plt.title('First Class-Needs')
plt.show()

#线下线上售卖情况
pivot_table_sales_chan = read_csv1.pivot_table(index=['sales_chan_name'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_sales_chan)
plt.bar(x=pivot_table_sales_chan.index,height=pivot_table_sales_chan['ord_qty'])
plt.xlabel('Order Type')
plt.ylabel('Order Amount')
plt.title('Order Type-Needs')
plt.show()

#细类画图
pivot_table_sales_second_cate = read_csv1.pivot_table(index=['second_cate_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_sales_second_cate)
plt.bar(x=pivot_table_sales_second_cate.index,height=pivot_table_sales_second_cate['ord_qty'])
plt.title('Second Class-Needs')
plt.xlabel('Second Class')
plt.ylabel('Order Amount')
x = range(401,413,1)
plt.xticks(x)
plt.show()


#按照季度分类画图
read_2015_3 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2015年第三季度.csv')
read_2016_1 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2016年第一季度.csv')
read_2016_2 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2016年第二季度.csv')
read_2016_3 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2016年第三季度.csv')
read_2017_1 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2017年第一季度.csv')
read_2017_2 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2017年第二季度.csv')
read_2017_3 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2017年第三季度.csv')
read_2018_1 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2018年第一季度.csv')
read_2018_2 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2018年第二季度.csv')
read_2018_3 = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\Data Mining Projects 分季度统计数据\2018年第三季度.csv')

#统计每个季度的销售总数
sum_plot = {'2015_3':sum(read_2015_3['11']),
            '2016_1':sum(read_2016_1['484']),
            '2016_2':sum(read_2016_2['26']),
            '2016_3':sum(read_2016_3['38']),
            '2017_1':sum(read_2017_1['38']),
            '2017_2':sum(read_2017_2['66']),
            '2017_3':sum(read_2017_3['11']),
            '2018_1':sum(read_2018_1['23']),
            '2018_2':sum(read_2018_2['21']),
            '2018_3':sum(read_2018_3['4'])}

print(sum_plot)
plt.bar(x=sum_plot.keys(),height=sum_plot.values(),color='y')
plt.xticks(rotation=45)
plt.title('Seasons Sales')
plt.xlabel('Year-Seasons')
plt.ylabel('Sales')
plt.show()

#统计季度一样,年份不一样
#第三季度
sum_plot_season_3 = {'2015_3':sum(read_2015_3['11']),
                     '2016_3':sum(read_2016_3['38']),
                     '2017_3':sum(read_2017_3['11']),
                     '2018_3':sum(read_2018_3['4'])}

plt.bar(x=sum_plot_season_3.keys(),height=sum_plot_season_3.values(),color='red')
plt.xticks(rotation=45)
plt.title('Seasons Three Sales')
plt.xlabel('Year-Seasons')
plt.ylabel('Sales')
plt.show()

#第二季度
sum_plot_season_2 = {'2016_2':sum(read_2016_2['26']),
                     '2017_2':sum(read_2017_2['66']),
                     '2018_2':sum(read_2018_2['21'])}

plt.bar(x=sum_plot_season_2.keys(),height=sum_plot_season_2.values(),color='red')
plt.xticks(rotation=45)
plt.title('Seasons Two Sales')
plt.xlabel('Year-Seasons')
plt.ylabel('Sales')
plt.show()

#第一季度
sum_plot_season_1 = {'2016_1':sum(read_2016_1['484']),
                     '2017_1':sum(read_2017_1['38']),
                     '2018_1':sum(read_2018_1['23'])}

plt.bar(x=sum_plot_season_1.keys(),height=sum_plot_season_1.values(),color='red')
plt.xticks(rotation=45)
plt.title('Seasons One Sales')
plt.xlabel('Year-Seasons')
plt.ylabel('Sales')
plt.show()

#线性回归开始










