import math
import numpy as np
import matplotlib.pyplot as plt

n_list = [1,10,50,100]

### Obtain the Y values for each X value in each function and plot the result ###

## n! (factorial)
y1 = np.array([math.factorial(n) for n in n_list])
## 2^n
y2 = np.array([2**n for n in n_list])
## n²
y3 = np.array([n**2 for n in n_list])
## sqrt(n)
y4 = np.array([math.sqrt(n) for n in n_list])
## log10(n)
y5 = np.array([math.log10(n) for n in n_list])

# Plot
plt.plot(n_list, y1, label='n!')
plt.plot(n_list, y2, label='2^n')
plt.plot(n_list, y3, label='n²')
plt.plot(n_list, y4, label='sqrt(n)')
plt.plot(n_list, y5, label='log10(n)')
plt.xlim(1, 100)
plt.ylim(1, 50)
plt.legend()
plt.show()



