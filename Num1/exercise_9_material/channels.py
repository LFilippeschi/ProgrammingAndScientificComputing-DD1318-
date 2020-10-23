import matplotlib.pyplot as plt
import imageio


im = imageio.imread('Num1/exercise_9_material/images/city.jpg')

im_0 = im.copy()
im_0[:,:,1:] = 0
plt.imshow(im_0)
plt.show()

plt.imshow(im[:,:,1])
plt.show()

plt.imshow(im[:,:,2])
plt.show()

plt.imshow(im)
plt.show()