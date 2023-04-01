import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#数据存储位置
weekend_2015_list = []#2015年星期天总和数据
Everyweek_data_weekday_2015_sum_count_list = []#2015年工作日数据处理后的数据
Everyweek_data_weekday_2016_sum_count_list = []
weekend_2016_list = []
Everyweek_data_weekday_2017_sum_count_list = []
weekend_2017_list = []
Everyweek_data_weekday_2018_sum_count_list = []
weekend_2018_list = []


#2015年数据处理
Data_2015_weekday = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2015年工作日.csv')
Data_2015_weekend = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2015年周末.csv')

Data_2015_weekday.columns = ['1','2','3','4']
Data_2015_weekend.columns = ['1','2','3','4']

k_2015_weekday = max(Data_2015_weekday['4'])
k_min_2015_weekday  = min(Data_2015_weekday['4'])
for i in range(k_min_2015_weekday,k_2015_weekday):
    Everyweek_data_weekday_2015 = Data_2015_weekday[Data_2015_weekday['4'] == i]
    Everyweek_data_weekday_2015_sum_count = Everyweek_data_weekday_2015['2'].sum()/5#核心数据
    for a in range(2):
        Everyweek_data_weekday_2015_sum_count_list.append(Everyweek_data_weekday_2015_sum_count)

#周末数据处理
k_2015_weekend = max(Data_2015_weekend['4'])
k_min_2015_weekend = min(Data_2015_weekend['4'])
for j in range(k_min_2015_weekend,k_2015_weekend):
    Everyweek_data_weekend_2015 = Data_2015_weekend[Data_2015_weekend['4'] == j]

    Saturday_order_amount_2015 = Everyweek_data_weekend_2015[Everyweek_data_weekend_2015['3'] == 5]
    Saturday_order_amount_2015_sum = Saturday_order_amount_2015['2'].sum()

    Sunday_order_amount_2015 = Everyweek_data_weekend_2015[Everyweek_data_weekend_2015['3'] == 6]
    Sunday_order_amount_2015_sum = Sunday_order_amount_2015['2'].sum()
    for b in range(1):
        weekend_2015_list.append(Sunday_order_amount_2015_sum)
        weekend_2015_list.append(Saturday_order_amount_2015_sum)


#2016年数据处理
Data_2016_weekday = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2016年工作日.csv')
Data_2016_weekend = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2016年周末.csv')

Data_2016_weekday.columns = ['1','2','3','4']
Data_2016_weekend.columns = ['1','2','3','4']

k_2016_weekday = max(Data_2016_weekday['4'])
k_min_2016_weekday  = min(Data_2016_weekday['4'])
for i in range(k_min_2016_weekday,k_2016_weekday):
    Everyweek_data_weekday_2016 = Data_2016_weekday[Data_2016_weekday['4']==i]
    Everyweek_data_weekday_2016_sum_count = Everyweek_data_weekday_2016['2'].sum()#核心数据
    for h in range(2):
        Everyweek_data_weekday_2016_sum_count_list.append(Everyweek_data_weekday_2016_sum_count)


#周末数据处理
k_2016_weekend = max(Data_2016_weekend['4'])
k_min_2016_weekend = min(Data_2016_weekend['4'])
for j in range(k_min_2016_weekend,k_2016_weekend):
    Everyweek_data_weekend_2016 = Data_2016_weekend[Data_2016_weekend['4'] == j]

    Saturday_order_amount_2016 = Everyweek_data_weekend_2016[Everyweek_data_weekend_2016['3'] == 5]
    Saturday_order_amount_2016_sum = Saturday_order_amount_2016['2'].sum()

    Sunday_order_amount_2016 = Everyweek_data_weekend_2016[Everyweek_data_weekend_2016['3'] == 6]
    Sunday_order_amount_2016_sum = Sunday_order_amount_2016['2'].sum()
    for c in range(1):
        weekend_2016_list.append(Saturday_order_amount_2016_sum)
        weekend_2016_list.append(Sunday_order_amount_2016_sum)




#2017年数据处理
Data_2017_weekday = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2017年工作日.csv')
Data_2017_weekend = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2017年周末.csv')

Data_2017_weekday.columns = ['1','2','3','4']
Data_2017_weekend.columns = ['1','2','3','4']

k_2017_weekday = max(Data_2017_weekday['4'])
k_min_2017_weekday  = min(Data_2017_weekday['4'])
for i in range(k_min_2017_weekday,k_2017_weekday):
    Everyweek_data_weekday_2017 = Data_2017_weekday[Data_2017_weekday['4']==i]
    Everyweek_data_weekday_2017_sum_count = Everyweek_data_weekday_2017['2'].sum()#核心数据
    for e in range(2):
        Everyweek_data_weekday_2017_sum_count_list.append(Everyweek_data_weekday_2017_sum_count)


#周末数据处理
k_2017_weekend = max(Data_2017_weekend['4'])
k_min_2017_weekend = min(Data_2017_weekend['4'])
for j in range(k_min_2017_weekend,k_2017_weekend):
    Everyweek_data_weekend_2017 = Data_2017_weekend[Data_2017_weekend['4'] == j]

    Saturday_order_amount_2017 = Everyweek_data_weekend_2017[Everyweek_data_weekend_2017['3'] == 5]
    Saturday_order_amount_2017_sum = Saturday_order_amount_2017['2'].sum()

    Sunday_order_amount_2017 = Everyweek_data_weekend_2017[Everyweek_data_weekend_2017['3'] == 6]
    Sunday_order_amount_2017_sum = Sunday_order_amount_2017['2'].sum()
    for w in range(1):
        weekend_2017_list.append(Saturday_order_amount_2017_sum)
        weekend_2017_list.append(Sunday_order_amount_2017_sum)


#2018年数据处理
Data_2018_weekday = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2018年工作日.csv')
Data_2018_weekend = pd.read_csv(r'C:\Users\14380\Desktop\Data Mining Projects\每一年工作日周末销售数量\2018年周末.csv')

Data_2018_weekday.columns = ['1','2','3','4']
Data_2018_weekend.columns = ['1','2','3','4']

k_2018_weekday = max(Data_2018_weekday['4'])
k_min_2018_weekday  = min(Data_2018_weekday['4'])
for i in range(k_min_2018_weekday,k_2018_weekday):
    Everyweek_data_weekday_2018 = Data_2018_weekday[Data_2018_weekday['4']==i]
    Everyweek_data_weekday_2018_sum_count = Everyweek_data_weekday_2018['2'].sum()#核心数据
    for l in range(2):
        Everyweek_data_weekday_2018_sum_count_list.append(Everyweek_data_weekday_2018_sum_count)

#周末数据处理
k_2018_weekend = max(Data_2018_weekend['4'])
k_min_2018_weekend = min(Data_2018_weekend['4'])
for j in range(k_min_2018_weekend,k_2018_weekend):
    Everyweek_data_weekend_2018 = Data_2018_weekend[Data_2018_weekend['4'] == j]

    Saturday_order_amount_2018 = Everyweek_data_weekend_2018[Everyweek_data_weekend_2018['3'] == 5]
    Saturday_order_amount_2018_sum = Saturday_order_amount_2018['2'].sum()

    Sunday_order_amount_2018 = Everyweek_data_weekend_2018[Everyweek_data_weekend_2018['3'] == 6]
    #print(Sunday_order_amount_2018)
    Sunday_order_amount_2018_sum = Sunday_order_amount_2018['2'].sum()
    for k in range(1):
        weekend_2018_list.append(Saturday_order_amount_2018_sum)
        weekend_2018_list.append(Sunday_order_amount_2018_sum)


#利用pandas制作表格(字典创建)


