import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1000)

databeta = np.random.beta(1,100, size=5000000)
databeta*=1000
bin = np.arange(1, 100, 1)

plt.hist(databeta, bin, color="red")
plt.title("try to make beta")
plt.tight_layout()
plt.show()