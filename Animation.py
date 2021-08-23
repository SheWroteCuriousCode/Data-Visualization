
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

x_data = []
y_data = []
fig, ax = plt.subplots()
ax.set_xlim (0, 110)
ax.set_ylim (0, 15)
line, = ax.plot(0, 0)

def init():
    line.set_data([], [])
    return line,


def animate (i):
    x_data.append (i * 10)
    y_data.append (i)
    
    line.set_xdata (x_data)
    line.set_ydata (y_data)
    return line,
    

anim = FuncAnimation(fig, animate, init_func=init, frames=np.arange (0,10,0.01), interval=10 )
plt.show()
HTML(anim.to_html5_video())