import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,2000)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel(f"angle {x}")
plt.ylabel(f"value of sin{x}")
plt.title("Sine function")
plt.legend(["sine"])
plt.grid(True)

plt.show()