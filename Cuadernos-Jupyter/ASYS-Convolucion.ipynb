{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "from matplotlib import animation\n",
    "import plotly.tools as tls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# First set up the figure, the axis, and the plot element we want to animate\n",
    "fig = plt.figure()\n",
    "XMAX = 10\n",
    "ax = plt.axes(xlim=(0, XMAX), ylim=(-0.1, 3))\n",
    "eje_x = [1,2,3]\n",
    "my_xticks = ['Fede', 'Fer', 'Ari']\n",
    "plt.xticks(eje_x, my_xticks)\n",
    "\n",
    "line, = ax.plot([], [], lw=2)\n",
    "\n",
    "\n",
    "# initialization function: plot the background of each frame\n",
    "def init():\n",
    "    line.set_data([], [])\n",
    "    return line,\n",
    "\n",
    "# animation function.  This is called sequentially\n",
    "def animate(t):\n",
    "    x = np.linspace(0, XMAX, 100)\n",
    "    y = np.piecewise(x, [x<(t/10), (x>(t/10)+1) & (x<(t/10)+2), x>(t/10)+2], [lambda x: 0,lambda x: x , lambda x: 0]) \n",
    "    line.set_data(x, y)\n",
    "    print (t)\n",
    "    return line,\n",
    "\n",
    "\n",
    "# call the animator.  blit=True means only re-draw the parts that have changed.\n",
    "anim = animation.FuncAnimation(fig, animate, init_func=init,\n",
    "                               frames=XMAX*10, interval=100, blit=True)\n",
    "\n",
    "# save the animation as an mp4.  This requires ffmpeg or mencoder to be\n",
    "# installed.  The extra_args ensure that the x264 codec is used, so that\n",
    "# the video can be embedded in html5.  You may need to adjust this for\n",
    "# your system: for more information, see\n",
    "# http://matplotlib.sourceforge.net/api/animation_api.html\n",
    "#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
