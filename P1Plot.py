import numpy as np
import matplotlib.pyplot as plt

def f(t):
  return np.sin(2 * np.pi * t / 5 + 0.2)

def secant_tangent(f, t_1, t_2):
  """
  Approximates the tangent slope to the function f at the point t using the secant method.

  Args:
    f: The function to approximate the tangent slope of.
    t_1: A point on the function curve.
    t_2: Another point on the function curve.

  Returns:
    The approximate tangent slope to the function f at the point t.
  """
  return (f(t_2) - f(t_1)) / (t_2 - t_1)

# Create a list of t values
t = np.linspace(0, 10, 1000)

# Calculate the f(t) values
y = f(t)

# Create a list with two periods of the f(t) values
f_list = np.concatenate((y, y))

# Calculate the tangent slopes at each point using the secant method
tangent_slopes = np.zeros(len(t_list))
for i in range(len(t_list) - 1):
  tangent_slopes[i] = secant_tangent(f, t_list[i], t_list[i + 1])

# Find the points where the tangent slope is closest to zero
zero_crossing_indices = np.where(np.abs(tangent_slopes) < 0.01)

# Extract the t and f(t) values at the zero crossings
zero_crossing_t = t_list[zero_crossing_indices]
zero_crossing_f = f(zero_crossing_t)

# Plot the points (t,f(t))
plt.plot(t_list, f_list)

# Plot the points where the tangent slope is closest to zero
plt.plot(zero_crossing_t, zero_crossing_f, 'o', color='red')

# Add labels and title
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Plot of f(t)=sin(2*pi*t/5 + 0.2) with zero crossings marked (secant method)')

# Show the plot
plt.show()
