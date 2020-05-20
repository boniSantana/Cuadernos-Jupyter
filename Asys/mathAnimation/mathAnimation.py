"""
Basado en: Matplotlib Animation Example
author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
"""
import matplotlib
matplotlib.use ('cairo')
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button, RadioButtons

plt.style.use('dark_background')

class Plot:
    def __init__(self, fig, ax):

        self.endPoint = 1000
        self.currentFrame = 0 
        self.fig = fig

        self.ax = ax
        self.line, = ax.plot([], [], lw=2)
        self.point, = ax.plot([], [], color='xkcd:lightish blue', marker='o', linestyle='dashed')

        self.x = np.linspace(0, 10, self.endPoint)

        self.y = 2/3 * pow(np.e, (-1/2)*self.x) * np.cos((pow(3, 0.5)/2) * self.x) - (2/3) * pow(np.e, -2*self.x)
        
        self.firsTime = True

    def set_value (self, frame=0):
        frame = int(frame)
        self.currentFrame = frame  ##  el valor del slider al de la animación
        if (self.firsTime == False):
            self.animation.event_source.stop()
        else:
            self.firsTime = True
        print("entre")
        self.animation = animation.FuncAnimation(self.fig, self.update, 99, interval=10, repeat_delay=5000, repeat=True, blit=False)

    def update(self, frame):
        frame = self.currentFrame
        '''No deberían ser necesarias estas 3 lineas, pero no se resetea adecuadamente la animación'''
        if (frame == 1000): # si termino
            self.animation.event_source.stop()
            return self.line, self.point
            
        else:
            self.line.set_data(self.x[0:frame], self.y[0:frame]) # actualizar valor line
            self.point.set_data(self.x[frame],self.y[frame]) # actualizar valor point
            # self.slider.set_val(frame) # actualizar valor slider # Si lo descomento entra constantemente a set_value, cosa que esta MAL
            self.currentFrame += 1 # siguiente frame
            print("currentFrame", self.currentFrame)
            print("Despues", frame)
            return self.line, self.point
    
    def animateSlider(self):
        slider_ax = self.fig.add_axes((0.1, 0.025, 0.5, 0.04))
        self.slider = Slider(slider_ax, label='Time',
                                  valmin=0, valmax=self.endPoint,
                                  valinit=0.0)
        
        self.slider.on_changed(self.set_value) ## listener, cuando cambie el slider

        plt.show()
    
    def save(self):
        self.animation = animation.FuncAnimation(self.fig, self.update, 99, interval=10, repeat_delay=5000, repeat=True, blit=False)
        self.animation.save('animation.gif', writer='imagemagick', fps=60)

    

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-2, 2))

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

myPlot = Plot (fig, ax)
myPlot.animateSlider()
myPlot.save()



