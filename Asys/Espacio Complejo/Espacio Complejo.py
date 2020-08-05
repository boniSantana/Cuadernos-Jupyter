"""
Basado en: Matplotlib Animation Example
author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
"""
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button, RadioButtons

fig = plt.figure()

ax = fig.add_subplot(2, 1, 1)
ax.set_title('centered spines')

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid()


R = 1
W = np.arange(0.1,40,0.01)
C = 1
L = 6

Z = R + 1 / 1j *(W*L - 1 / W*C)


print (Z.real, "+", Z.imag, "j")

ax.scatter(Z.real, Z.imag)


Z2 = 1/Z

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_title('centered spines')

ax2.spines['left'].set_position('center')
ax2.spines['right'].set_color('none')
ax2.spines['bottom'].set_position('center')
ax2.spines['top'].set_color('none')
ax2.spines['left'].set_smart_bounds(True)
ax2.spines['bottom'].set_smart_bounds(True)
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.grid()

plt.scatter(Z2.real , Z2.imag)


plt.show()