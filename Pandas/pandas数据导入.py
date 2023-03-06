import pandas as pd
import numpy as np
import openpyxl
import pymysql

#读取csv文件
csv1 = pd.read_csv(r"C:\Users\14380\Desktop\douban.csv",encoding="utf-8",header=0,sep=',')
#print(csv1)
#encoding为编码模式,headers是指定第几行作为列名,sep和delimiter为指定对应隔号

csv2 = pd.read_csv(r"C:\Users\14380\Desktop\douban.csv",encoding='utf-8',names=['test 1','test 2'],header=0)
print(csv2)#names即指定colums的names

#存档csv文件
#csv2.to_csv(r'C:\Users\14380\Desktop\test.csv')#电脑桌面会有奇迹发生

#读取excel
#excel_test1 = pd.read_excel(r"C:\Users\14380\Desktop\重庆市少年儿童图书馆招募工作\2022年重庆少图文化志愿服务队时长统计(1)(1).xlsx",sheet_name=0)#默认第一页
#print(excel_test1)
#excel_test2 = pd.read_excel(r"C:\Users\14380\Desktop\重庆市少年儿童图书馆招募工作\2022年重庆少图文化志愿服务队时长统计(1)(1).xlsx",sheet_name=[0,1])
#print(excel_test2)
#print(excel_tese2['Sheet2'])以此类推
#excel_test3 =  pd.read_excel(r"C:\Users\14380\Desktop\重庆市少年儿童图书馆招募工作\2022年重庆少图文化志愿服务队时长统计(1)(1).xlsx",sheet_name=None)#None就是全部读取


#读取一列并创建series
#excel_test4 = pd.read_excel(r"C:\Users\14380\Desktop\重庆市少年儿童图书馆招募工作\2022年重庆少图文化志愿服务队时长统计(1)(1).xlsx",sheet_name=0)
#print(excel_test4)
#data = pd.Series(excel_test4['姓名'])
#print(data)

#设置index_col和header
excel_test5 = pd.read_excel(r"C:\Users\14380\Desktop\重庆市少年儿童图书馆招募工作\2022年重庆少图文化志愿服务队时长统计(1)(1).xlsx",sheet_name=0,header=[0,2],index_col=0)#删减header和index_col来进行比较
#print(excel_test5)#其实这里设置一个index_col有点像去除默认的index

#存档excel文件
excel_test5.to_excel(r'C:\Users\14380\Desktop\test.xlsx',sheet_name='test name')

#读取Mysql中的文件
#connection = pymysql.connect(host='localhost',user='root',password='masaike',db='light',charset='utf8')#连接数据库
#sql_code = 'select * from table' #直接输入sql语句
#datas = pd.read_sql(connection,sql_code)


