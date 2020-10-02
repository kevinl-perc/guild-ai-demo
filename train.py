import numpy as np

# Hyperparameters
x = 0.1
noise = 0.1

loss = (np.sin(5*x) * (1-np.tanh(x ** 2)) + np.random.randn() * noise)

print(f"loss: {loss}")