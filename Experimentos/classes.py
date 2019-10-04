import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from typing import Tuple

XMIN = -1
XMAX = 5
YMIN = -0.1
YMAX = 6

# First set up the figure, the axis, and the plot element we want to animate
fig: Figure = plt.figure() # fig es de tipo figure
ax: Axes = plt.axes(xlim=(XMIN, XMAX), ylim=(YMIN, YMAX))

line: Line2D = ax.plot([], [], lw=2)[0]
line2: Line2D = ax.plot([], [], lw=2)[0]
rect = Rectangle((0,0), 1, 1, 0, color='none')
ax.add_patch(rect)
# initialization function: plot the background of each frame
def init(): # -> Tuple[Line2D] significa que retorna eso.
    line.set_data([], [])
    line2.set_data([], [])

    return (line, line2, rect) # es una tupla: array invariable.

# animation function.  This is called sequentially
def animate(t):

    x: np.ndarray = np.linspace(XMIN, XMAX, 1000)
    # t takes values between 0 and 200, we need values between XMIN, XMAX
    t_scaled = t/20 + XMIN
    y1 = x * 0
    np.place(y1, (x>t_scaled) & (x<t_scaled+2), [2])

    y2 = 1*x - 2 #si pongo x se rompe...

    np.place(y2,(x>3) | (x<2), [0])

    plt.fill_between(x,y2,y1,where = (y1 < y2), color = 'g', interpolate = True)
#
#    if ( 0 < t_scaled and t_scaled < 1):
#        rect.set_color('green')
#        rect.set_width( 1 - t_scaled)
#        rect.set_x(t_scaled)
#
#    if ( -1 < t_scaled and t_scaled < 0):
#        rect.set_color('green')
#        rect.set_width(t_scaled + 1)
#        if (rect.get_x() != 0):
#            rect.set_x(0)

    line.set_data(x, y1)
    line2.set_data(x, y2)

    return (line, line2, rect)


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
plt.show()


# To save the animation, use the command: line_ani.save('lines.mp4')
