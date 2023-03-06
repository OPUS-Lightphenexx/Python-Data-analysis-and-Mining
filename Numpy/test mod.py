from numpy计算笔记 import fill_ndarray
import numpy as np

new_test = np.arange(24).reshape((4,6)).astype('float')
#print(new_test)
new_test[2,3:]=np.nan
print(new_test)

print(fill_ndarray(new_test))