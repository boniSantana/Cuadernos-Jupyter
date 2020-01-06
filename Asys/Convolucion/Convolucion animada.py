import plotly.tools as tls
from matplotlib import animation
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import sympy as sp
import shapely as sh
from shapely.geometry import Polygon

matplotlib.use('Qt5Agg')

## Función escalon u(t).
def u(t):
    return np.piecewise(t,t>=0,[1,0])

# Figura.
fig = plt.figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')

# Eje.
XMAX = 30
XMIN = -10
YMIN = -2
YMAX = 15
ax = plt.axes(xlim=(XMIN, XMAX), ylim=(YMIN, YMAX))

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# tiempo [a,b], muestras, dt.
a = -5 ; b = 5 ; muestras = 101 ; dt = 0.01



#Preparo los valores de la función que se moverá (señal de entrada)

def x(t):
    return 10*np.exp(-3*t)*u(t)

x_move_initial = np.linspace(a, b, muestras)
y_move = np.flip(x(x_move_initial))
y_move[-1] = 0
y_move[0] = 0

#Preparo los valores de la función estática (respuesta al escalón)

def h(t):
    return (2*np.exp(-2*t)-np.exp(-t))*u(t)

x_static = np.linspace(5, 10, muestras)
y_static = h(x_static)
y_static[0] = 0
y_static [-1] = 0


# Integral de Convolucion x[t]*h[t]
dt = 0.01
y_convolve = np.convolve(y_move,y_static,'same')*dt


#Cargo a init las dos líneas vacias
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

# Inicializo el poligono vacío que luego rellenará el area.
polygone = ax.fill_between(x_static[0:0], y_static[0:0], facecolor='yellow', alpha=0.5)
polygone2 = ax.fill_between(x_static[0:0], y_static[0:0], facecolor='yellow', alpha=0.5)

#Distancia entre dos puntos de X_static.
velocidad = (x_static[6]-x_static[5])

# Funcion que inicia la animación
def init():
    line.set_data([], [])
    line2.set_data([x_static], [y_static])
    return line, line2, polygone, polygone2

# Función animación, es llamada cíclicamente.

def animate(t):

    x_move_t = np.copy(x_move_initial)

    
    # x = xinicial + v*t
    x_move_t = x_move_initial + velocidad*t

    ax.collections.clear() # Sino no funciona el rellenado correctamente
    
    t_encuentro_maximo_minimo = int((x_static[0]-x_move_initial[-1])/velocidad)
    t_encuentro_minimo_minimo = int((x_static[0]-x_move_initial[0])/velocidad)
   

    # Si se encuentran:
    if (t >= t_encuentro_maximo_minimo) and (t <= t_encuentro_minimo_minimo):
        polygone = ax.fill_between(
            x_static[0:(t-t_encuentro_maximo_minimo)],
            y_static[0:(t-t_encuentro_maximo_minimo)],
            color = 'lightpink', 
            alpha = 0.4, 
            hatch = '/',
        )
        polygone2 = ax.fill_between(
            np.flip(x_move_t)[0:(t-t_encuentro_maximo_minimo)],
            np.flip(y_move)[0:(t-t_encuentro_maximo_minimo)],
            color = 'lightgreen', 
            alpha = 0.4, 
            hatch = '|',
        )

    elif (t > t_encuentro_minimo_minimo):

        
        polygone = ax.fill_between(
            x_static[(t-t_encuentro_minimo_minimo)::],
            y_static[(t-t_encuentro_minimo_minimo)::],
            color = 'lightpink', 
            alpha = 0.4, 
            hatch = '/',
        )
        polygone2 = ax.fill_between(
            np.flip(x_move_t)[(t-t_encuentro_minimo_minimo)::],
            np.flip(y_move)[(t-t_encuentro_minimo_minimo)::],
            color = 'lightgreen', 
            alpha = 0.4, 
            hatch = '|',
        )
    
    else:
        polygone = ax.fill_between(x_static[0:0], y_static[0:0], facecolor='yellow', alpha=0.5)
        polygone2 = ax.fill_between(x_static[0:0], y_static[0:0], facecolor='yellow', alpha=0.5)
        
    line.set_data(x_move_t, y_move)
    
    return line, line2, polygone, polygone2


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=int((round((XMAX-b)/velocidad)))
, interval=10, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=300, extra_args=['-vcodec', 'libx264'])

plt.show()
