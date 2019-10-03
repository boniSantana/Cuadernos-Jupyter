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
fig = plt.figure()
XMAX = 10
ax = plt.axes(xlim=(0, XMAX), ylim=(-0.1, 3))
eje_x = [1,2,3]
my_xticks = ['Fede', 'Fer', 'Ari']
plt.xticks(eje_x, my_xticks)

line, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(t):
    x = np.linspace(0, XMAX, 100)
    y = np.piecewise(x, [x<(t/10), (x>(t/10)+1) & (x<(t/10)+2), x>(t/10)+2], [lambda x: 0,lambda x: x , lambda x: 0]) 
    line.set_data(x, y)
    print (t)
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=XMAX*10, interval=100, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
