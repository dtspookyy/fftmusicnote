import numpy as np
import matplotlib.pyplot as plt
import scipy
from numpy.ma.core import argmax

from scipy.io import wavfile
samplerate, data = wavfile.read("oneSecondNote.wav")

xt = data
freqs = np.fft.fftfreq(len(xt), d=1/48000)
midpoint = len(xt)//2

fxt = np.fft.fft(xt)
magnitude = abs(fxt)
plt.plot(freqs[:midpoint], magnitude[:midpoint])
plt.title("Plot of FFT of x(t)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

ind = np.argpartition(magnitude, -50)[-50:]
top50 = magnitude[ind]

fxtReduced = np.zeros_like(fxt)
fxtReduced[ind] = fxt[ind]

xtReconstructed = np.fft.ifft(fxtReduced)
xtReconstructedReal = np.real(xtReconstructed)
plt.plot(xtReconstructedReal)
plt.title("Plot of Reconstructed FFT of x(t)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.show()


