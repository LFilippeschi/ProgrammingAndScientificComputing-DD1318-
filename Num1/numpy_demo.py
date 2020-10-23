import numpy as np
import matplotlib.pyplot as plt

import time

# CHECK HERE https://docs.scipy.org/doc/numpy/

if __name__ == '__main__':
    my_list = [2, 8, 4, 16]
    my_nparray = np.array(my_list)

    # Operators
    print('my_list*2', my_list * 2)
    print('my_nparray*2', my_nparray * 2)

    # Constant arrays
    print('np.arange(0, 2, 0.2)', np.arange(0, 2, 0.2))
    print('np.zeros(4)', np.zeros(4))
    print('np.ones(5) *4', np.ones(5) * 4)

    # Selection
    print('my_nparray[2:4]', my_nparray[2:4])
    print('my_nparray[my_nparray> 4]', my_nparray[my_nparray > 4])

    # Attributes
    print('Shape: ', my_nparray.shape)
    print('Datatype: ', my_nparray.dtype)
    print('Size: ', my_nparray.size)
    print('Num Dimensions: ', my_nparray.ndim)

    # Datatypes
    my_nparray = np.array(my_list, dtype='float')
    print(' np.array(list2, dtype=\'float\')', my_nparray)
    print('my_nparray.astype(\'int\')', my_nparray.astype('int'))

    # Reshaping
    my_nparray = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    print('my_nparray.reshape(4, 2)', my_nparray.reshape(4, 2))

    # Transposing
    my_nparray = np.array([[0, 1, 2], [3, 4, 5]])
    transposed = my_nparray.transpose()
    print('my_nparray.transpose()')
    print(transposed)
    print('Shape comparison', my_nparray.shape, transposed.shape)

    # Matrix Operations
    a = [[1, 2], [3, 4]]
    b = [[1, 0], [0, 1]]
    mat_a = np.array(a)
    mat_b = np.array(b)

    print(np.matmul(mat_a, mat_b))  # proper matrix multiplication
    print(np.multiply(mat_a, mat_b))  # element-wise multiplication

    # Maximum
    a = np.arange(4).reshape((2, 2))
    print('np.amax(a)', np.amax(a))
    print('np.amax(a, axis=0)', np.amax(a, axis=0))

    # Plotting
    x = np.arange(20)
    y2 = 4 * x
    y1 = x * x
    fig, ax = plt.subplots()
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.grid()
    ax.set(xlabel='x', ylabel='y', title='About as simple as it gets, folks')
    fig.savefig("test.png")
    plt.show()

    # Trigonometry Plotting
    sample_rate = 0.01
    t = np.arange(0.0, 3.14, sample_rate)
    s = 1 + np.sin(np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Sample rate example')
    ax.grid()

    fig.savefig("test_sin.png")
    plt.show()

    # Performance - Convolution

    sample_rate = 0.001
    x = np.arange(0.0, 3.14, sample_rate)
    data = 1 + np.sin(np.pi * x)
    noise = np.random.normal(0, 0.1, x.size)
    noisy_data = data + noise
    filt = np.array([0.06, 0.24, 0.39, 0.24, 0.06])
    # filt = np.array([0, 1, 0])

    start_time = time.time()
    smoothed_data = np.convolve(noisy_data, filt, 'same')
    print('np.convolve() took', time.time() - start_time, 'milliseconds.')

    start_time = time.time()
    manual_smooth = np.zeros(x.size)
    for i in range(x.size):
        pos0 = noisy_data[i - 2] if i > 1 else 0
        pos1 = noisy_data[i - 1] if i > 0 else 0
        pos2 = noisy_data[i]
        pos3 = noisy_data[i + 1] if i < x.size - 1 else 0
        pos4 = noisy_data[i + 2] if i < x.size - 2 else 0

        manual_smooth[i] = 0.06 * pos0 + 0.24 * pos1 + 0.39 * pos2 + 0.24 * pos3 + 0.06 * pos4
    print('manual convolution took', time.time() - start_time, 'milliseconds.')

    fig, ax = plt.subplots()
    ax.plot(x, noisy_data)
    ax.plot(x, smoothed_data)
    ax.plot(x, manual_smooth)
    ax.grid()
    plt.show()
