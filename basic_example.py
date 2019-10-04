"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import plotly.tools as tls
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')

XMAX = 10
ax = plt.axes(xlim=(0, XMAX), ylim=(-0.1, 10))
#eje_x = [1,2,3,4,5,6,7,8,9,10]
#my_xticks = ['t', 't-1', 't-2', 't-3', 't-4', 't-5', 't-6', 't-7', 't-8', 't-9']
#plt.xticks(eje_x, my_xticks)

line, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(t):
    
    x: np.ndarray = np.linspace(0, XMAX, 1000)
    z: np.ndarray = np.copy(x)
    y: np.ndarray = np.piecewise(x, [x<3, (x>=3) & (x<=7), x>7], [lambda x: 0,lambda x: x , lambda x: 0]) 
    z: np.ndarray = z + ((t/100)%3)
    print("Z =", z[-1])
    if (z[-1] >= XMAX+3) : 
        z = np.copy(x)
        print (z[-1])
    
    line.set_data(z, y)
    print (t)
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=10, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
