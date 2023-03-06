import numpy as np

#创建数组
#a = np.array([1,2,3,4,5])
#b = np.array(range(1,6))
#c = np.arange(1,6)
#指定数据类型
#e = np.array([1,2,3,4,5])#后面加一个dtype=

#改变数据类型
#d = a.astype('int8')
#print(d.dtype)

#numpy中的小数
#t = np.array([np.random.random() for x in range(10)])
#print(t)

#取好多位数
#t1 = np.round(t,2)#数字为要取好多位数字

#数组的形状(有点像矩阵)
#a1 = np.array([[1,2,3,4,3,4],[3,2,3,5,4,3]])
#a1_1 = a1.shape
#修改数组的形状
#a2 = a1.reshape(3,4)
#变一维
#a3 = a1.flatten()

#快速获得
#a_s = np.arange(100,120).reshape(2,10)

#多维度计算,遵循广播原则
#(3,3,2)可以和(3,2)进行运算

#取行(只是个例子)
#print(a1[1])
#print(a1[1:])#连续多个行
#print(a1[[0,1]])#取不连续多个行

#取列,逗号隔开的后面就是列
#print(a1[1:,:])
#print(a1[[0,1],:])#取不连续多行
#print(a1[:,1])#取一列
#print(a1[:,1:])#取连续的多列
#print(a1[:,[0,1]])#取不连续的多列

#取行和列(这里是交叉的结果)
#print(a1[2:5,1:4])

#取多个不相邻的点
#这里对应的就是(0,0),(2,1),(2,3)
#print(a1[[0,1,1],[1,1,1]])


#numpy中数值的修改
#a1[1:,:]=2#直接赋值


#change = a1<3
#print(change)

#a1[a1<3]=4
#print(a1)

#the = a1[a1<4]
#print(the)

#numpy中的三元运算符号

#n = np.arange(24).reshape((4,6))
#n_change = np.where(n<10,0,10)#这里要注意了
#print(n)
#print(n_change)

#n_change_again = n.clip(10,20)
#print(n_change_again)

#数组的拼接
#changed = np.vstack((n_change,n_change_again))#竖直方向上的拼接
#print(changed)

#changed_1 = np.hstack((n_change,n_change_again))
#print(changed_1)

#数组的行列交换
#n[[1,2],:]=n[[2,1],:]#行变换
#print(n)
#n[:,[0,1]]=n[:,[1,0]]
#print(n)

#其他方法
#np.zeros((3,4))#全为0的数组
#np.ones((3,4))#全为1的数组
#np.eye(10)#对角数组

#numpy分割
#new_set1 = np.arange(12).reshape((3,4))
#print(new_set1)
#split1 = np.split(new_set1,4,axis=1)
#print(split1)

#new_set2 = np.arange(27).reshape(3,3,3)
#print(new_set2)

#print(new_set1)
#split2 = np.split(new_set1,2,axis=1)
#print(split2)
#转置
#set_again = np.arange(24).reshape((4,6))
#print(set_again)
#tans = set_again.transpose()
#print(tans)
#获取最大最小值的位置(按每一行每一列进行位置确定)
#np.argmax(n,axis=0)
#np.argmin(n,axis=1)

#numpy生成随机数(重点)
#np.random.seed(10)
#d1 = np.random.rand(2,3)
#d2 = np.random.randint(2,60,(3,4))
#d3 = np.random.randn(3,3)
#d4 = np.random.uniform(-3,3,(3,3))
#d5 = np.random.normal(3,2,(3,4))
#print(d1)
#print(d2)
#print(d3)
#print(d4)
#print(d5)

#数组复制
#a=b完全不影响
#a=b[:]#a由b影响
#a=b.copy()#独立了,成功复制

#nan的处理
#a_again = np.count_nonzero(a)
#print(a_again)
#计算nan的个数
#a_nan = np.count_nonzero(a!=a)#这里a!=a返回的是一个布尔值
#print(a!=a)
#print(a_nan)
#替代nan然后变成一个新的值
#t[np.isnan(t)]=2
#print(t)

#数组求和
#new_array = np.arange(12).reshape(3,4)
#print(new_array)

#new_array1 = np.sum(new_array,axis=0)#sum
#new_array2 = np.sum(new_array,axis=1)
#print(new_array1)
#print(new_array2)

#nice = new_array.mean(axis=0)#mean均值
#print(nice)

#median = np.median(new_array,axis=0)#中值
#print(median)

#ptp = np.ptp(new_array,axis=0)#极值,最大值与最小值之差
#print(ptp)

#std = np.std(new_array,axis=0)#标准差,有点忘了
#print(std)

#填充nan的方法

def func(new_test):
    for i in range(new_test.shape[1]):
        all_col = new_test[:,i]
    #print(all_col)
        count_col = np.count_nonzero(all_col!=all_col)#这里是一个整数
    #print(count_col)
        if count_col!=0:
        #print(count_col)
           kill_nan_col = all_col[all_col==all_col]
           #print(kill_nan_col)
           median = kill_nan_col.mean()
           #print(median)
           all_col[np.isnan(all_col)]=median
    return new_test

new_test = np.arange(24).reshape((4,6)).astype('float')
#print(new_test)
new_test[2,3:]=np.nan
#print(func(new_test))






