import numpy as np

#MAX VALUE

max = max(20, 72, 63, 900, 21, 0, 2)
min = min(20, 72, 63, 900, 21, 0, 2)

Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

mean = np.mean(Calorie_burnage)

print("max:", max)
print("min:", min)
print("mean:", mean)
