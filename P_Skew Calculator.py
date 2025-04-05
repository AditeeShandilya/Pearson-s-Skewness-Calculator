#Pearson's Skewness calculator(with graph)
import numpy as np
import matplotlib.pyplot as plt
n = int(input("how many observations do you want to input"))
a = []
for i in range(1,n+1):
    b = int(input(f'input the observation no.{i}'))
    a.append(b)
a = np.array(a)
mean = np.mean(a)
median = np.median(a)
std = np.std(a)
pskew = 3*((mean-median)/std)
print(pskew)
if pskew > 0:
    print("It is positively skewed")
elif pskew < 0:
    print('Its negatively skewed')
else:
    print("Its symmetric data")
plt.plot(a,range(1,n+1),color="lightseagreen")
plt.axvline(mean, linestyle = '-', color = 'turquoise', label = f'mean is {mean:.2f}')
plt.axvline(median,linestyle='--',color='lightblue', label = f'median is {median:.2f}')
plt.legend()
plt.grid(True)
plt.show()
