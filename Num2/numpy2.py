import cmath
import numpy as np
import matplotlib.pyplot as plt

count = 0

def mandelbrot(c):
    global count
    count = 0 
    z = complex(0,0)
    z = z * z + c
    for i in range(10000):
        z = z * z + c
        if abs(z) > 4:
            count = i
            return False
    count = i
    return True

###interesting center (-1.41, 0)   
xcenter = -0.7746806106269039
ycenter = -0.1374168856037867
for step in range(1,100):
    print("zoom x", 2**step)
    rate = 2**step
    amin = xcenter - 2/rate
    amax = xcenter + 2/rate
    aoffset = 0
    bmin = ycenter - 2/rate
    bmax = ycenter + 2/rate
    boffset = 0
    

    if amin < 0:
        aoffset = -amin
    else:
        aoffset = -amin

    if bmin < 0:
        boffset = -bmin
    else:
        boffset = -bmin


    M = np.zeros((2401, 2401))
    # print(M)
    a = np.linspace(amin, amax, 2400)
    #print(len(a))
    b = np.linspace(bmin, bmax, 2400)
    #print(len(b))
    for x in a:
        for y in b:
            mandelbrot( complex(x, y) )
            M[(int)( (y + boffset) *600*rate), (int)( ( x + aoffset) * 600*rate)] = count

    #print(len(M))

    #gist_ncar_r
    plt.imshow(M, cmap='gist_ncar_r', extent=(amin, amax, bmin, bmax))
    plt.axis('off')
    #plt.savefig('mandelbrot_images_2/mandelbrot_zoom_acc10000_{}.svg'.format(2**step), format='svg', dpi=1200)
    plt.show()
    
