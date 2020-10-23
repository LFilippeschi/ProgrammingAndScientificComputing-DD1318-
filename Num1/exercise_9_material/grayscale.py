import matplotlib.pyplot as plt
import imageio
import numpy as np

im = imageio.imread('Num1/exercise_9_material/images/city.jpg')

# print(im.dtype)

# can't do manual, because of overflow issues
# grayscale_im = (im[:,:,0] + im[:,:,1] + im[:,:,2]) / 3

grayscale_im = np.mean(im,axis=2)

plt.imshow(grayscale_im, cmap='Greys_r')
plt.show()