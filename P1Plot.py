import numpy as np
import matplotlib.pyplot as plt

def f(t):
  return np.sin(2*np.pi*t/5 + 0.2)

t = np.linspace(0, 2*np.pi*2, 1000)

f_values = f(t)

def tangent_slope(t):
  h = 0.1
  return (f(t + h) - f(t)) / h

tangent_slopes = tangent_slope(t)

min_index = np.argmin(np.abs(tangent_slopes))
max_index = np.argmax(np.abs(tangent_slopes))

# Print the t and f(t) values at the points where the tangent slope is closest to zero
print('Minimum tangent slope:')
print('t:', t[min_index])
print('f(t):', f(t[min_index]))

print('Maximum tangent slope:')
print('t:', t[max_index])
print('f(t):', f(t[max_index]))

plt.plot(t, f_values)

plt.title('f(t) = sin(2*pi*t/5 + 0.2)')
plt.xlabel('t')
plt.ylabel('f(t)')

plt.plot(t[min_index], f(t[min_index]), 'ro')
plt.plot(t[max_index], f(t[max_index]), 'bo')

plt.show()

