import numpy as np
import matplotlib.pyplot as plt 
import plotly.plotly as py
import plotly.tools as tls

mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)

names = ['-4T', '-3T', '-2T', '-T' ]
values = [-4,-3,-2,-1]
x = np.linspace(0, 10, 100)


# lambda es una función anonima que retorna lo que sigue a :
y = np.piecewise(x, [x<3, (x>3) & (x<5), x>5], [lambda x: 0,lambda x: 1, lambda x: 1]) 
y2 = x**2
print (x)
print (y)
plt.plot(x, y, '-', lw=2)

plt.bar(names, values)
plt.axis([-5, 10, -0.5, 2])
 
plt.show()