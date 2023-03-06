import pandas as pd
import numpy as np

#导入数据
covid_Data_total = pd.read_csv('covidtotals.csv')
print(covid_Data_total)
print('-'*100)

#判断数据大小
print(covid_Data_total.shape)
print('-'*100)
#判断数据类型
print(covid_Data_total.dtypes)
print('-'*100)

#检查索引值是否唯一
print(covid_Data_total.index.nunique())
print('-'*100)

#用info判断non-null(非空值)
print(covid_Data_total.info())
print('-'*100)

#随机抓取
print(covid_Data_total.sample(2).T)#T为转置,方便查看数据
print('-'*100)












