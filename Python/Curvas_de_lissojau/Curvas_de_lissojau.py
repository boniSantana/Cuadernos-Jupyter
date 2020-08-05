import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation

def trayectoria(fase, amplitud, v_angular, t):
    return amplitud * np.sin ((v_angular * t)+ fase)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
   
tiempo = 5000
 
xdata = []
ydata = []
 
# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,
 
# animation function.  This is called sequentially
def animate(t):

    global xdata
    global ydata

    A = 2.8
    B = 3

    t_scaled = -np.pi + (t * (np.pi * 2)) / 1000 

    delta = np.pi / 2
    gamma = 0
    amplitud = 1
    decaimiento = 0.02
    
   # Foucault pendulus
   # x = np.cos(A * t_scaled) * np.cos(5* t_scaled) * (amplitud)
   # y = np.sin(A * t_scaled) * np.cos(5*t_scaled) * (-amplitud)


    x = np.sin(A * t_scaled + delta) * (amplitud * np.power(np.e, -(decaimiento * t_scaled)))
    y = np.sin(B * t_scaled + gamma) * (amplitud * np.power(np.e, -(decaimiento * t_scaled)))

    xdata.append(x)
    ydata.append(y)
    
    if ((t -1)% tiempo == 0):
        xdata = []
        ydata = []


 
    line.set_data(xdata, ydata)
    return line,
 
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=tiempo, interval=2, blit=True)
 
# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=100, extra_args=['-vcodec', 'libx264'])
 
plt.show()