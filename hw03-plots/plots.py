import matplotlib.pyplot as plt
import numpy as np

def summation(n):
     i = 0
     result = 0
     while i <= 4:
          if n - i >= 0:
               result += 1
          i+=1
     return result
x = [i for i in range(-10,10)]
y = [0] * 10
y1 = [1] * 10

plt.stem(x, y + y1)
plt.xticks(np.arange(-6,12,2))
plt.yticks(np.arange(0,1.5,0.5))
plt.show()

n = [i for i in range(-5,11)]
y_2b = [0] * len(n)
i = 0
while i < len(n):
     y_2b[i] = (1.0/5.0)*summation(n[i])
     print("y[%d] = %f" % (i, y_2b[i]))
     i += 1

plt.stem(n,y_2b)
plt.xticks(np.arange(-6,12,2))
plt.yticks(np.arange(0,1.5,0.5))
plt.show()
