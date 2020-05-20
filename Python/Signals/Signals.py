import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['text.usetex'] = True

sns.set(style="white")

A = 1
w = 1
fase = 1 * np.pi

XMIN = -5
XMAX = 5


t = np.linspace(XMIN, XMAX, 1000)  # two cycles, 100 points each

y = np.sign(A * np.sin(( w * 2*np.pi*t) + fase ))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 3))


ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.xaxis.set_ticks_position('none') # tick markers
ax.yaxis.set_ticks_position('none')

# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
#plt.ylim(0, 90)
#plt.xlim(1968, 2014)
ax.tick_params(labelsize=14)


# Make sure your axis ticks are large enough to be easily read.
# You don't want your viewers squinting to read your plot.
ax.set_yticks([-1, 0, 1])
ax.set_xticks(np.linspace(XMIN, XMAX, 3))

ax.set_xlim(-7,7)

ax.set_ylim(-1.2,1.2)


# Capa 0
ax.axhline(y=1, xmin=0, xmax=1, ls="--", lw=0.5, color="black", alpha=0.3)
ax.axhline(y=-1, xmin=0, xmax=1, ls="--", lw=0.5, color="black", alpha=0.3)

# Capa 1
ax.plot(t, y, solid_capstyle="round",
           solid_joinstyle="round", lw=1.5)

# Capa 2

xmin, xmax = ax.get_xlim() 
ymin, ymax = ax.get_ylim()

hw = 1./80.*(ymax-ymin) 
hl = 1./80.*(xmax-xmin)
lw = 0.5 # axis line width
ohg = 0.1 # arrow overhang

dps = fig.dpi_scale_trans.inverted()
bbox = ax.get_window_extent().transformed(dps)
width, height = bbox.width, bbox.height

# compute matching arrowhead length and width
yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width 
yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw = lw, 
         head_width=hw, head_length=hl, overhang = ohg, 
         length_includes_head= True, clip_on = False) 

ax.arrow(0, ymin, 0., ymax-ymin, fc='k', ec='k', lw = lw, 
         head_width=yhw, head_length=yhl, overhang = ohg, 
         length_includes_head= True, clip_on = False) 

ax.annotate(r't[s]', (XMAX, -0.2))


plt.show()
