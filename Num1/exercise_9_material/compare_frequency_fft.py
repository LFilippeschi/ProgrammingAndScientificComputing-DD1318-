import scipy.io.wavfile
import scipy.fft
import numpy as np
import matplotlib.pyplot as plt

sample_rate_1, samples_1 = scipy.io.wavfile.read('Num1/exercise_9_material/audio/piano.wav')
sample_rate_2, samples_2 = scipy.io.wavfile.read('Num1/exercise_9_material/audio/260.wav')

fft_1 = scipy.fft.fft(samples_1)
fft_2 = scipy.fft.fft(samples_2)
frequencies_1 = scipy.fft.fftfreq(fft_1.size, 1/sample_rate_1)
frequencies_2 = scipy.fft.fftfreq(fft_2.size, 1/sample_rate_2)

plt.plot(scipy.fft.fftshift(frequencies_1),
         scipy.fft.fftshift(abs(fft_1)), label='piano')
plt.plot(frequencies_2, abs(fft_2), label='synthetic')
plt.legend()
plt.show()