import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# produce the line point, the distance is consistent
# x1 = np.linspace(0.0, 5.0)
# x2 = np.linspace(0.0, 2.0)

# produce the continuous point
x1 = np.arange(0.0, 5.0, 0.01)
x2 = np.arange(0.0, 2.0, 0.01)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

# (2, 1)表示2行1列的图
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('A tale of 2 subplots')

# 加上o-代表对曲线进行描点  不加上 o-代表不描点（看起来会比较平滑）
# ax1.plot(x1, y1, 'o-')
ax1.plot(x1, y1)
ax1.set_ylabel('Damped oscillation')


# 同上
# ax2.plot(x2, y2, '.-')
ax2.plot(x2, y2)
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')

# 表示加上网格
ax1.grid()
ax2.grid()


plt.show()