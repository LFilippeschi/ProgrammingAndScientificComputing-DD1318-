import matplotlib.pyplot as plt
import imageio
import numpy as np
import time

def is_green(color):
    if color[1] > color[0] and color[1] > color[2]:
        return True
    else:
        return False

spiderman = imageio.imread('../images/spiderman.png')
city = imageio.imread('../images/city.jpg')

# simple for loop
t0 = time.time()
for x in range(0,spiderman.shape[0]):
    for y in range(0, spiderman.shape[1]):
        if not is_green(spiderman[x,y,:]):
            city[x,y,:] = spiderman[x,y,:]
t1 = time.time()
delta_python = t1-t0
print(delta_python)

            
# using numpy logic
t0 = time.time()
mask = np.logical_and(spiderman[:,:,1] > spiderman[:,:,0],
                      spiderman[:,:,1] > spiderman[:,:,2])
city[~mask,:] = spiderman[~mask,:]
t1 = time.time()
delta_numpy = t1-t0
print(delta_numpy)


print(f'NumPy version {delta_python / delta_numpy} times faster.')


plt.imshow(city)
plt.show()
imageio.imwrite('../images/result.jpg', city)