import matplotlib.pyplot as plt

#a = ['f','s','fu','woc']#be nice <_<

#b = [2,5,7,3]

#plt.figure(figsize=(10,10),dpi=80)

#plt.bar(a,b,width=0.3)
#plt.xticks(a,a,rotation=45)

#plt.savefig('./picture.png')

#绘制横着的条形图
#a = ['f','s','fu','woc']#be nice <_<

#b = [2,5,7,3]

#plt.figure(figsize=(10,10),dpi=80)
#plt.barh(a,b)
#plt.yticks(a,a,rotation=45)
#plt.grid()

#绘制多个条形图
a = ['nice','good','very good ','freak']
b_1 = [15746,312,4497,319]
b_2 = [12357,156,2045,168]
b_3 = [2358,399,2358,362]

x_1 = list(range(len(a)))
x_2 = [i+0.2 for i in x_1]
x_3 = [i-0.2 for i in x_1]


plt.bar(x_2,b_2,width=0.2,label='1')
plt.bar(a,b_3,width=0.2,label='2')
plt.bar(x_3,b_1,width=0.2,label='3')

plt.xticks(x_1,a)#手动设置即可,a即为标识

plt.legend()#图标

plt.show()
