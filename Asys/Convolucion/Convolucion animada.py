import plotly.tools as tls
from matplotlib import animation
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')

class function:

    def __init__(self, conditionArray, Xfunc):
        self.conditionArray = conditionArray
        self.Xfunc = Xfunc
        self.x = np.linspace(self.Xfunc[0]-0.01, self.Xfunc[1]+0.01, self.Xfunc[2])

    def __str__(self):
        return str("Aca voy a poner en el JupyterNotebook algo cool para mostrar tipo Latex la ec")

    def Xvalues(self):
        return self.x

    def Condition(self):
        return [self.x < self.Xfunc[0], (self.x >= self.Xfunc[0]) & (self.x <= self.Xfunc[1]), self.x > self.Xfunc[2]]

    def setFunctions(self, func1, func2, func3):
        return [lambda f:func1, lambda f:func2, lambda f:func3]

    def Yvalues(self, functions):
        return np.piecewise(self.x, self.Condition(), functions)

    def lastX(self):
        return self.Xfunc[1]



# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(num=None, figsize=(14, 6), dpi=80,
                 facecolor='w', edgecolor='k')

def func1(x):
    return 2*x

def func2(x):
    return 2*x

movefunction = function([2, 11], [2, 4, 1000])

Functions =movefunction.setFunctions(
    func1(movefunction.Xvalues()),
    func2(movefunction.Xvalues()),
    0)

staticfunction = function([7.5, 11], [7.5, 11, 1000])
FunctionsStatic = staticfunction.setFunctions(0, 2, 0)

XMAX = 20
desplazamiento = XMAX - movefunction.lastX()

ax = plt.axes(xlim=(0, XMAX), ylim=(-0.1, 50))
#eje_x = [1,2,3,4,5,6,7,8,9,10]
#my_xticks = ['t', 't-1', 't-2', 't-3', 't-4', 't-5', 't-6', 't-7', 't-8', 't-9']
#plt.xticks(eje_x, my_xticks)

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

x2 = staticfunction.Xvalues()
y2 = staticfunction.Yvalues(FunctionsStatic)
polygone = ax.fill_between(x2[0:0], y2[0:0], facecolor='yellow', alpha=0.5)

# initialization function: plot the background of each frame


def init():
    line.set_data([], [])
    line2.set_data([x2], [y2])
    return line, line2, polygone

# animation function.  This is called sequentially


def animate(t):

    x_func = movefunction.Xvalues()
    f_x = movefunction.Yvalues(Functions)
    z = np.copy(x_func)

    z = z + (t/100)

    ax.collections.clear()

    # Si la parte más a la derecha de la funcion que se mueve es mayor que la parte de mas a la izquierda de la estatica:
    if (z[-1] >= x2[0]):
        polygone = ax.fill_between(
            x2[0:2*(t-348)],
            y2[0:2*(t-348)],
            facecolor='yellow',
            alpha=0.5)

    else:
        polygone = ax.fill_between(
            x2[0:0],
            y2[0:0],
            facecolor='yellow',
            alpha=0.5)
    # sin el else no anda, se referencia antes de que se llame, no entiendo por que.

    line.set_data(z, f_x)
    return line, line2, polygone


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=desplazamiento * 100, interval=5, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
