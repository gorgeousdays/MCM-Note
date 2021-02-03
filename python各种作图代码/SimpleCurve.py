import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# fig is the return picture, ax is the coordinate
fig, ax = plt.subplots()
ax.plot(t, s)

# set xlabel ,ylabel and the table title
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')

# display the grid
ax.grid()

# save the result
fig.savefig("test.png")

# show the result
plt.show()