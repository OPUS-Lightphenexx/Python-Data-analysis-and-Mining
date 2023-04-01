import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#各年同季度

#第一季度
#2016年第一季度
Season_1_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2016年第一季度.csv')
Season_1_2016_ord = Season_1_2016_Data['484'].sum()

#2017年第一季度
Season_1_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2017年第一季度.csv')
Season_1_2017_ord = Season_1_2017_Data['38'].sum()

#2018年第一季度
Season_1_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2018年第一季度.csv')
Season_1_2018_ord = Season_1_2018_Data['23'].sum()

#各年第一季度画图开始
height_season_1 = np.array([Season_1_2016_ord,Season_1_2017_ord,Season_1_2018_ord])
plt.bar(x=[1,2,3],height=height_season_1)
labels_season_1 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_1)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season One Sales')
plt.grid()
plt.show()


#第二季度
#2016年第二季度
Season_2_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2016年第二季度.csv')
Season_2_2016_ord = Season_2_2016_Data['11'].sum()

#2017年第二季度
Season_2_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2017年第二季度.csv')
Season_2_2017_ord = Season_2_2017_Data['673'].sum()

#2018年第二季度
Season_2_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2018年第二季度.csv')
Season_2_2018_ord = Season_2_2018_Data['18'].sum()

#各年第二季度画图开始
height_season_2 = np.array([Season_2_2016_ord,Season_2_2017_ord,Season_2_2018_ord])
plt.bar(x=[1,2,3],height=height_season_2)
labels_season_2 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_2)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Two Sales')
plt.grid()
plt.show()


#第三季度
#2016年第三季度
Season_3_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2016年第三季度.csv')
Season_3_2016_ord = Season_3_2016_Data['54'].sum()

#2017年第三季度
Season_3_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2017年第三季度.csv')
Season_3_2017_ord = Season_3_2017_Data['6'].sum()

#2018年第三季度
Season_3_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2018年第三季度.csv')
Season_3_2018_ord = Season_3_2018_Data['6'].sum()

#各年第三季度画图开始
height_season_3 = np.array([Season_3_2016_ord,Season_3_2017_ord,Season_3_2018_ord])
plt.bar(x=[1,2,3],height=height_season_3)
labels_season_3 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_3)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Three Sales')
plt.grid()
plt.show()



#第四季度
#2016年第四季度
Season_4_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2016年第四季度.csv')
Season_4_2016_ord = Season_4_2016_Data['263'].sum()

#2017年第四季度
Season_4_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2017年第四季度.csv')
Season_4_2017_ord = Season_4_2017_Data['51'].sum()

#2018年第四季度
Season_4_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\季度统计\2018年第四季度.csv')
Season_4_2018_ord = Season_4_2018_Data['14'].sum()

#各年第四季度画图开始
height_season_4 = np.array([Season_4_2016_ord,Season_4_2017_ord,Season_4_2018_ord])
plt.bar(x=[1,2,3],height=height_season_4)
labels_season_4 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_4)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Four Sales')
plt.grid()
plt.show()

