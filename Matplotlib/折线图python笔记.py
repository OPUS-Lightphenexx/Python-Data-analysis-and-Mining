#折线图笔记
import matplotlib.pyplot as plt
import numpy as np
import pandas as pb

#绘制折线图基础
#x = range(2,26,2)
#y = [1,2,3,4,5,6,7,8,9,19,11,12]

#plt.plot(x,y)

#设置图片大小并保存图片
#fig = plt.figure(figsize=(20,8),dpi=80)
#plt.savefig('example')


#设置x和y轴的刻度
#ticks = [i/2 for i in range(4,52)]
#plt.xticks(ticks[::3],'标签',rotation=90)
#plt.yticks()

#xtick_labels = ["{}岁".format(i) for i in x]
#plt.xticks(x, xtick_labels, fontproperties=my_font)
#plt.yticks(range(0,11))


#random
#x = range(0,120)
#cent = {i:np.random.randint(0,120) for i in range(120)}
#y = [b for b in cent.values()]
#plt.plot(x,y)

#绘制两条线
#x = range(1,5)
#y_1 = [1,3,4,3]
#y_2 = [4,6,2,6]
#plt.plot(x,y_1,label='nice',color='blue',linestyle=':')
#plt.plot(x,y_2,label='nice2',linestyle='--')
#绘制网格
plt.grid()#(透明度 alpha=0.2)
#图例
plt.legend()#对应label#plt.legend(loc=0)对应的是图标位置
#终极show
plt.show()


