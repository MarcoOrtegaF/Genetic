import matplotlib.pyplot as plt
import numpy as np

def f(t):
  return np.sin(2 * np.pi * t / 5 + 0.2)

t = np.linspace(0, 10, 100)

y = f(t)

plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("f(t) = sin(2*pi*t/5 + 0.2)")
plt.show()

# Find the points where the slope of the tangent is closest to zero.
# We can do this by approximating the tangent using the secant.

for i in range(len(y) - 1):
  secant_slope = (y[i + 1] - y[i]) / (t[i + 1] - t[i])
  if abs(secant_slope) < 1e-5:
    plt.plot(t[i], y[i], "*", color="red")
    plt.plot(t[i + 1], y[i + 1], "*", color="red")

plt.show()