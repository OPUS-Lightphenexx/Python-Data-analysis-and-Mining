import pandas as pd
import numpy as np
import string

#一维series的创建
series1 = pd.Series(np.arange(0,10),index=list(string.ascii_uppercase[0:10]))
print(series1)
series2 = pd.Series([1,2,3,4,5])
print(series2)
series3 = pd.Series([1,2,3,4,5],index=(list("abcde")))#这里注意用的是字符串list
print(series3)
#用字典的方法创建series
series4 = pd.Series({'dog':'cute','cat':'bad'})
print(series4)

#series的切片与索引(以series1为例子)
series1_1test = series1[list("ABC")]
print(series1_1test)
series1_2test = series1[2:10:2]
print(series1_2test)
series1_3test = series1[2:4]
print(series1_3test)
series1_4test = series1[['A','C']]#注意这里还是要用到list
print(series1_4test)
series1_5test = series1[[2,3,5]]
print(series1_5test)
series1_6test = series1[series1>=4]
print(series1_6test)

#series中的index和values
series1_test_index = series1.index
print(series1_test_index)
series1_test_values = series1.values
print(series1_test_values)

#测试where用法
series1_where_test = series1.where(series1>4)
print(series1_where_test)
series1_where_test2 = series1.where(series1>4,10)#后面那个10就是填充nan值
print(series1_where_test2)

