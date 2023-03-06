import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#导入数据并查看每一列
Main_covid_data = pd.read_csv(r"C:\Users\14380\Desktop\covidtotals.csv")
print(Main_covid_data)

#综合数据
Data_Describe = Main_covid_data.describe()
print(Data_Describe)

#看有多少是非空值
Data_info = Main_covid_data.info()
print(Data_info)

#基于pandas绘图
#Main_covid_data['median_age'].plot(kind='line')
#Main_covid_data['median_age'].plot(kind='box')
#plt.show()


#数据透视
#频数统计(一维)
value_count = Main_covid_data['hosp_beds'].value_counts()
print(value_count)

#cut_count1 = pd.cut(Main_covid_data['hosp_beds'],bins=10).value_counts().plot(kind='bar')
#cut_count2 = pd.cut(Main_covid_data['hosp_beds'],bins=[1,2,3,4]).value_counts().plot(kind='bar')
print(max(Main_covid_data['hosp_beds'].value_counts()))
#plt.show()
#print(cut_count2)

#列连表(二维)频数统计(数据给的不恰当,当个例子就行)
crosstab_count3 = pd.crosstab(Main_covid_data['location'],Main_covid_data['median_age'],margins=True)
crosstab_count4 = pd.crosstab(Main_covid_data['location'],Main_covid_data['median_age'],margins=True,normalize='columns')#这个代表比列
crosstab_count5 = pd.crosstab(Main_covid_data['location'],Main_covid_data['median_age'],margins=True,normalize='index')
crosstab_count6 = pd.crosstab(Main_covid_data['location'],Main_covid_data['median_age'],margins=True,normalize='all')
print(crosstab_count4)
print(crosstab_count5)

#画图(只是个例子,不然图回卡爆)
#crosstab_plot1 = crosstab_count3.plot(kind='bar')
#crosstab_plot2 = crosstab_count3.plot(kind='bar',stacked=True)
#plt.show()

#groupby计量数据的聚集
groupby_data1 = Main_covid_data.groupby(['lastdate']).count()
groupby_data2 = Main_covid_data.groupby(['lastdate']).size()
groupby_data3 = Main_covid_data.groupby(['lastdate'])['gdp_per_capita'].mean()
print(groupby_data1)
print(groupby_data2)
print(groupby_data3)
#多个聚合
groupby_data4 = Main_covid_data.groupby(['lastdate','location'])['hosp_beds'].count()
print(groupby_data4)

#pivot_table进行多维度透视分析(高级点,以上面groupby对应)
Pivot_table1 = Main_covid_data.pivot_table(index=['lastdate','location'],values=['hosp_beds'],aggfunc=len)
print(Pivot_table1)
Pivot_table2 = Main_covid_data.pivot_table(index=['lastdate','location'],values=['hosp_beds'],aggfunc=[len,np.mean])
print(Pivot_table2)
Pivot_table3 = Main_covid_data.pivot_table(index=['lastdate'],values=['hosp_beds'],aggfunc=len)#看来pivot_table适合多维度透视分析,单个频率统计就用value_count吧
print(Pivot_table3)
#Pivot_table复合数据的透视(就是更多应用)
#添加合计margins
Pivot_table4 = Main_covid_data.pivot_table(index=['lastdate','location'],values=['hosp_beds'],aggfunc=[len,np.mean],margins=True,margins_name='total')#margins为底部总的汇总数据
print(Pivot_table4)
Pivot_table5 = Main_covid_data.pivot_table(index=['lastdate','location'],values=['hosp_beds','gdp_per_capita'],aggfunc=[len,np.mean])
print(Pivot_table5)#搞不懂values为啥是反着的








