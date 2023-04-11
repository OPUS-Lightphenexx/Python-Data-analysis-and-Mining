import matplotlib.pyplot as plt
import numpy as np

np.random.seed(102)
data_test_1 = np.random.randint(0, 100, 10)

print(data_test_1)

plt.violinplot(dataset=data_test_1, showmeans=True, vert=True)
plt.title('Violin Plot Test 1')
plt.grid()
plt.show()


data_test_2 = np.random.normal(size=1000)
print(data_test_2)

plt.violinplot(dataset=data_test_2,showmeans=True)
plt.title('Violin Plot Test 2')
plt.grid()
plt.show()


data_test_3 = np.random.random(1000)
print(data_test_3)

plt.violinplot(dataset=data_test_3,showmeans=True,showmedians=True)
plt.title('Violin Plot Test 4')
plt.grid()
plt.show()

data_test_4 = [data_test_3,data_test_2]
plt.violinplot(data_test_4,showmeans=True)
plt.title('Violin Plot Test 4')
plt.grid()
plt.show()

#优化处理过后的violin plot
data_test_5_another_1 = np.random.normal(size = 1000)
data_test_5_another_2 = np.random.normal(size = 1000)
data_test_5_another_3 = np.random.normal(size = 2000)
data_test_5_list = [data_test_5_another_1,
               data_test_5_another_2,
               data_test_5_another_3]
plt.violinplot(data_test_5_list,showmeans=True)
plt.title('Violin Plot Test 4')
plt.xticks([i+1 for i in range(len(data_test_5_list))],['Data 1','Data 2','Data 3'])
plt.grid()
plt.show()

#用subplot进行画图(参考官网)
pos = [1]
data1 = [data_test_1]
data2 = [data_test_2]
data3 = [data_test_3]
data4 = [data_test_5_another_1]

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

axs[0, 0].violinplot(data1, pos, points=20, widths=0.3,showmeans=True, showextrema=True, showmedians=True)
axs[0, 0].set_title('Violin Plot Test 1')
axs[0, 0].grid()


axs[0,1].violinplot(data2,pos,points=20,widths=0.4,showmeans=True,showextrema=True,showmedians=True)
axs[0,1].grid()
axs[0,1].set_title('Violin Plot Test 2')

axs[1,0].violinplot(data3,pos,points=20,widths=0.4,showmeans=True,showextrema=True,showmedians=True)
axs[1,0].grid()
axs[1,0].set_title('Violin Plot Test 3')

axs[1,1].violinplot(data4,pos,points=20,widths=0.4,showmeans=True,showextrema=True,showmedians=True)
axs[1,1].grid()
axs[1,1].set_title('Violin Plot Test 4')

plt.show()


