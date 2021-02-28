import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from sensor import value

global ALL_RAW_BPM

style.use('fivethirtyeight')


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    ALL_RAW_BPM.append(f'{len(ALL_RAW_BPM)},{value()}')
    xs = []
    ys = []
    for line in ALL_RAW_BPM:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs,ys)

ALL_RAW_BPM = []

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()

