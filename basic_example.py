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

XMAX = 20
MAXVALUEFUNC = 4
desplazamiento = XMAX - MAXVALUEFUNC
MINVALUEFUNC = 2

MINVALUEFUNC2 = 7.5
MAXVALUEFUNC2 = 11
i = 0
ax = plt.axes(xlim=(0, XMAX), ylim=(-0.1, 50))
#eje_x = [1,2,3,4,5,6,7,8,9,10]
#my_xticks = ['t', 't-1', 't-2', 't-3', 't-4', 't-5', 't-6', 't-7', 't-8', 't-9']
#plt.xticks(eje_x, my_xticks)

line, = ax.plot([], [], lw=2)
line2, = ax.plot ([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    x2: np.ndarray = np.linspace(MINVALUEFUNC2-0.01, MAXVALUEFUNC2+0.01, 1000)
    y2: np.ndarray = np.piecewise(x2, [x2<MINVALUEFUNC2, (x2>=MINVALUEFUNC2) & (x2<=MAXVALUEFUNC2), x2>MAXVALUEFUNC2], [lambda x: 0,lambda x: 2*x , lambda x: 0]) 
    line2.set_data([x2], [y2])
    return line,

# animation function.  This is called sequentially
def animate(t):

    x2: np.ndarray = np.linspace(MINVALUEFUNC2-0.01, MAXVALUEFUNC2+0.01, 1000)
    y2: np.ndarray = np.piecewise(x2, [x2<MINVALUEFUNC2, (x2>=MINVALUEFUNC2) & (x2<=MAXVALUEFUNC2), x2>MAXVALUEFUNC2], [lambda x: 0,lambda x: 2*x , lambda x: 0]) 

    x: np.ndarray = np.linspace(MINVALUEFUNC-0.01, MAXVALUEFUNC+0.01, 1000)
    z: np.ndarray = np.copy(x)
    y: np.ndarray = np.piecewise(x, [x<MINVALUEFUNC, (x>=MINVALUEFUNC) & (x<=MAXVALUEFUNC), x>MAXVALUEFUNC], [lambda x: 0,lambda x: x**2 , lambda x: 0]) 
    z: np.ndarray = z + (t/100)

    x2: np.ndarray = np.linspace(MINVALUEFUNC2-0.01, MAXVALUEFUNC2+0.01, 1000)
    
    ax.collections.clear()
     
    #348 
    if (z[-1] >= x2[0]):
        print ("Dentro:", t)
        polygone = ax.fill_between (x2[0:2*(t-348)] ,y2[0:2*(t-348)], facecolor='yellow', alpha=0.5)
    
    else:
        print ("Fuera:", t)
        polygone = ax.fill_between (x2[0:0] ,y2[0:0], facecolor='yellow', alpha=0.5)

    if (z[-1] >= XMAX+XMAX-MAXVALUEFUNC) : 
        z = np.copy(x)

    line.set_data(z, y)

    return line, polygone


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames= desplazamiento * 100, interval=10, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

#Si ymove>yquieto pinto yquieto,
#Sino pinto ymove
#Mientras haya intersección:
#Si ymove>yquieto pinto yquieto,
#Sino pinto ymove
#Una variable que guarde un array de condiciones y otro un array de funciones
#Y un intervalo donde graficar en X la función
#Una clase llamada funcion que le pasas las condiciones y las funciones y las escribe correctamente
#Adentro tiene el piecewise directamentee
#Los parametros para inicializarla son:
#1. Un np.ndarray de valores de X.
#2. Un array de funciones
#3. Un array de condiciones

#Los metodos son:
#yvalues()
#xvalues()
#
#
#
#
