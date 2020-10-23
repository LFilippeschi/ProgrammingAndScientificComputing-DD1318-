import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

sample_rate, samples = scipy.io.wavfile.read('Num1/exercise_9_material/audio/260.wav')
scipy.io.wavfile.write('Num1/exercise_9_material/audio/260_double.wav', sample_rate*2, samples)
scipy.io.wavfile.write('Num1/exercise_9_material/audio/260_half.wav', sample_rate//2, samples)