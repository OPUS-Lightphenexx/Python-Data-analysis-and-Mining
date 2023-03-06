import pandas as pd
import numpy as np

#结合numpy创建DataFrame
DataFrame_test1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['test1','test2','test3','test4'],index=['01','02','03'])
print(DataFrame_test1)

#字典形式创建DataFrame
Dict_test_1 = {'name':['light','phenexx'],'id':['1','2'],'order':['gov','cent']}
DataFrame_test2 = pd.DataFrame(Dict_test_1)
#print(DataFrame_test2)
#list中加入字典
Dict_test_2 = [{'name':'light','id':1,'order':'gov'},{'name':'phenexx','id':'2','order':'cent'}]
Dict_test_3 = pd.DataFrame(Dict_test_2)
print(Dict_test_3)

#DataFrame的基础属性(以DataFrame_test1为例子)
shape = DataFrame_test1.shape
print(shape)
print('*'*100)
index = DataFrame_test1.index
print(index)
print('*'*100)
datatype = DataFrame_test1.dtypes
print(datatype)
print('*'*100)
dimension = DataFrame_test1.ndim
print(dimension)
print('*'*100)
columns = DataFrame_test1.columns
print(columns)
print('*'*100)
values = DataFrame_test1.values#生成numpy形式
print(values)
print('*'*100)
#整体情况查询(head和tail默认值为5行)
head_search = DataFrame_test1.head(2)
print(head_search)
print('*'*100)
tail_search = DataFrame_test1.tail(1)
print(tail_search)
print('*'*100)
info = DataFrame_test1.info()
print(info)
print('*'*100)
describe = DataFrame_test1.describe()#得出综合数据
print(describe)


#DataFrame排序(True为从小到大,False为从大到小)
order = DataFrame_test1.sort_values(by='test1',ascending=False)
print(order)
print(order.head(2))

#DataFrame取行和列
#print(DataFrame_test1)
select_test1 = DataFrame_test1[:2]['test1']
print(select_test1)#指定列数
select_test2 = DataFrame_test1['test2']#用colum name 进行取列
print(select_test2)
select_test3 = DataFrame_test1

#使用loc和iloc进行提取(区别是一个是标签一个是数字位置)
print(DataFrame_test1)
loc_select_test1 = DataFrame_test1.loc['01','test2']
print(loc_select_test1)
print('*'*100)
loc_select_test2 = DataFrame_test1.loc['01',['test1','test3']]
print(loc_select_test2)
loc_select_test3 = DataFrame_test1.loc[['01','02'],['test1','test3']]#一一对应取出
print(loc_select_test3)
loc_select_test4 = DataFrame_test1.loc['01':,'test2':]
print(loc_select_test4)
#iloc进行提取(参照上面loc)
print(DataFrame_test1)
print('*'*100)
iloc_select_test1 = DataFrame_test1.iloc[0,2]
print(iloc_select_test1)
iloc_select_test2 = DataFrame_test1.iloc[0,[0,2]]
print(iloc_select_test2)
iloc_select_test3 = DataFrame_test1.iloc[[0,1],[0,2]]
print(iloc_select_test3)
iloc_select_test4 = DataFrame_test1.iloc[0:,1:]
print(iloc_select_test4)

#DataFrame之赋值
print(DataFrame_test1)
DataFrame_test1.loc['01','test1']=2
print(DataFrame_test1)
DataFrame_test1.iloc[0,[0,2]] = 3
print(DataFrame_test1)

#布尔select
bool_select1 = DataFrame_test1[(DataFrame_test1['test3']>3)&(DataFrame_test1['test4']>7)]#&符号表示同时满足(且)
print(bool_select1)
bool_select2 = DataFrame_test1[(DataFrame_test1['test3']>200000000)|(DataFrame_test1['test4']>4)]#这个表示huo
print(bool_select2)

#DataFrame中字符串的处理之Split
DataFrame_test3 = pd.Series(['a/b/c','no/yes/no','test1/test2/test3'])
print(DataFrame_test3)
Split1 = DataFrame_test3.str.split('/')
print(Split1)
Split2 = DataFrame_test3.str.split('/').str.get(1)#指定列数
print(Split2)
Split3 = DataFrame_test3.str.split('/',expand=True)#变成DataFrame
print(Split3)
Split4 = DataFrame_test3.str.split('/',expand=True,n=1)
print(Split4)
Split5 = DataFrame_test3.str.rsplit('/',expand=True,n=1)#反向切割
print(Split5)

#处理方法之replace
print(DataFrame_test1)
replace_test1 = DataFrame_test1.replace(DataFrame_test1.loc['01','test1'],4,inplace=False)
print(replace_test1)
replace_test2 = DataFrame_test1.replace(4,1)#全局变换replace
print(replace_test2)
replace_test3 = DataFrame_test1.replace({3:4,1:0})#字典的形式进行变换replace
print(replace_test3)
replace_test4 = DataFrame_test1.replace({'test1':{3:4,4:3}})#但指向某一列
print(replace_test4)

#模糊查询replace
DataFrame_test4 =pd.DataFrame({'abc':['abcde','what'],'abcd':'avc'},index=['01','02'])
print(DataFrame_test4)
replace_test5 = DataFrame_test4.replace('b','test',regex=True)
print(replace_test5)
replace_test6 = DataFrame_test4.replace(regex='c',value='')
print(replace_test6)
DataFrame_test4['abcd'] = DataFrame_test4['abcd'].str.replace('c','2')#指定某个列然后模糊查询替换
print(DataFrame_test4)

#处理缺失值Nan
DataFrame_test5 = pd.DataFrame({'test':['?','^',np.nan,'3',np.nan,'$',np.nan,'?','$',np.nan,'56',np.nan,'$']})
print(DataFrame_test5)
#向前一个值进行填充
replace_test7 = DataFrame_test5.replace(np.nan,method='ffill')
print(replace_test7)
replace_test8 = DataFrame_test5.replace(np.nan,method='bfill')
print(replace_test8)
#limit的用法(非重点)
DataFrame_test6 = pd.DataFrame({'test':['?',np.nan,np.nan,np.nan,'5','6',np.nan,'5',np.nan,np.nan]})
print(DataFrame_test6)
replace_test9 = DataFrame_test6.replace(np.nan,method='ffill',limit=1)
print(replace_test9)
replace_test10 = DataFrame_test6.replace(np.nan,method='ffill',limit=2)
print(replace_test10)

#判断是否为nan

print(DataFrame_test1)
replace_side1 = DataFrame_test1.replace(DataFrame_test1.iloc[1,1:],np.nan)
print(replace_side1)
DataFrame_test1.iloc[1,1:] = np.nan
print(DataFrame_test1)

isnull1 = pd.isnull(DataFrame_test1)
print(isnull1)
notnull1 = pd.notnull(DataFrame_test1)
print(notnull1)

#删除nan所在行和列
print(DataFrame_test1)
#DataFrame_test1.dropna(axis=0,how='any',inplace=True)#变一变axis的值
#print(DataFrame_test1)

#用pandas填充nan值(fillna)
#DataFrame_test1 = DataFrame_test1.fillna(DataFrame_test1.median(),axis=0)
print(DataFrame_test1)
DataFrame_test1['test2'] = DataFrame_test1['test2'].fillna(DataFrame_test1['test2'].median())
print(DataFrame_test1)

#pandas concat进行数据拼接(默认纵向拼接)
#设置两个图表
np.random.seed(2)
numpy1 = np.array([[np.random.randint(0,20) for x in range(20)],[np.random.randint(0,20) for x in range(20)]])
numpy2 = np.array([[np.random.randint(0,20) for x in range(20)],[np.random.randint(0,20) for x in range(20)]])
numpy1.reshape((4,10))
numpy2.reshape(2,20)
DataFrame_test7 = pd.DataFrame(numpy1,columns=['{}号'.format(i) for i in range(20)],index=['01','02'])
DataFrame_test8 = pd.DataFrame(numpy2,columns=['{}号'.format(i) for i in range(20)],index=['01','02'])
DataFrame_test9 = pd.DataFrame(np.random.randn(3,4),columns=['A','B','C','D'])
DataFrame_test10 = pd.DataFrame()
print(DataFrame_test7)
print(DataFrame_test8)

joint_test1 = pd.concat([DataFrame_test7,DataFrame_test8])
print(joint_test1)
joint_test2 = pd.concat([DataFrame_test7,DataFrame_test8],axis=1)
print(joint_test2)
joint_test3 = pd.concat([DataFrame_test7,DataFrame_test8],axis=1,join='outer')
joint_test4 = pd.concat([DataFrame_test7,DataFrame_test8],axis=1,join='inner')#省略nan值

#异常值的处理
np.random.seed(2)
DataFrame_test11=pd.DataFrame(np.random.randn(1000,4))
print(DataFrame_test11)
Describe_test = DataFrame_test11.describe()
print(Describe_test)
#Error_Data1 = DataFrame_test11[(np.abs(DataFrame_test11)>3).any(1)]
#print(Error_Data1)#处理这样的异常数据就用numpy中的sign函数
#指定值
#DataFrame_test11[(np.abs(DataFrame_test11)>3).any(1)] = np.sign(DataFrame_test11)*3
#Error_Data1 = DataFrame_test11[(np.abs(DataFrame_test11)>3).any(1)]
#print(Error_Data1)
#print(DataFrame_test11.describe())
#删除异常列
DataFrame_test11.drop(DataFrame_test11[np.abs(DataFrame_test11)>3],axis=0,inplace=True)
print(DataFrame_test11)



#还有很多拼接方法,会在另一页解释,也有API可以查询

