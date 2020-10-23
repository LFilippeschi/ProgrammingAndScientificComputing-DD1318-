""" import cmath
z = complex(2,1)
print(z.real, z.imag)
z = z + 1j
print(abs(z))
print(cmath.phase(z))
print(cmath.polar(z)) """

import imageio
im = imageio.imread('test.png')

import matplotlib
import matplotlib.pyplot as plt
#im = plt.imread('test.png')
plt.imshow(im)
plt.show()