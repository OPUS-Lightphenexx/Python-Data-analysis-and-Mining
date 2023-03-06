import matplotlib.pyplot as plt
import pandas as pd

#y_1 = [1,5,7,3,6,5]
#y_2 = [5,3,7,5,7,3]

#x = range(0,6)

#plt.figure(figsize=(2,80),dpi=80)

#plt.scatter(x,y_1)
#plt.scatter(x,y_2)


#绘制分别两个
y_1 = [1,5,7,3,6,5]
y_2 = [5,3,7,5,7,3]

x_1 = range(0,6)
x_2 = range(8,14)

#plt.figure(figsize=(2,80),dpi=80)

plt.scatter(x_1,y_1,label='1')
plt.scatter(x_2,y_2,label='2')

#调整x轴的刻度
stick = [i*2 for i in range(8)]
plt.xticks(stick)

plt.legend(loc='best')

plt.show()
