import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-1, 5)
y = x.reshape(-1, 1)
y1 = np.arange(-1,5)
h = x**2 + y**2
print(x)
print(y)
print(h)

cs = plt.contourf(h,levels=[6,10],extend='both')
cs.cmap.set_over('red')
cs.cmap.set_under('blue')
cs.changed()

plt.show()