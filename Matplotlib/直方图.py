#先放一放


import matplotlib.pyplot as plt

a = [53,6,3,6,34,2,3,4,56,34,54,75,43,65,66,45,7,55,43,65,4,5,67,67,2]
num_bim = (max(a)-min(a))//2
plt.hist(a,bins=num_bim)
plt.xticks(num_bim)
plt.show()