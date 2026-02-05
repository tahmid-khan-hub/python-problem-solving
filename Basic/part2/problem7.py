''' Use numpy and matplotlib libraries to plot a sine wave from 0 to 3pi. '''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)

plt.plot(x, y)

plt.title("Sine Wave from 0 to 3π")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")

plt.grid(True)

plt.show()