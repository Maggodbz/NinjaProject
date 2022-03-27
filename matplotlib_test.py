import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt 


n = [1,2,3]
f = [np.sin(m) for m in n]
plt.plot(n,f,"r")
plt.show()