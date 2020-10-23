import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

sample_rate_1, samples_1 = scipy.io.wavfile.read('Num1/exercise_9_material/audio/piano.wav')
sample_rate_2, samples_2 = scipy.io.wavfile.read('Num1/exercise_9_material/audio/260.wav')

times_1 = np.linspace(0, samples_1.shape[0]/sample_rate_1, samples_1.shape[0], endpoint=False)
times_2 = np.linspace(0, samples_2.shape[0]/sample_rate_2, samples_2.shape[0], endpoint=False)


plt.plot(times_1, samples_1, label='Piano')
plt.plot(times_2, samples_2, label='Synthetic')
plt.legend()
plt.show()