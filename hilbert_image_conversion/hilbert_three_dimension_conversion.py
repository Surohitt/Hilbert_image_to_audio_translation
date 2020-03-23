from scipy.io.wavfile import write
import numpy as np
from hilbertcurve.hilbertcurve import HilbertCurve
from matplotlib.pyplot import *
import cv2

image = cv2.imread('suro.jpg')
dim = image.shape
center = round(dim[0]/2)
start = center-170
end = center+86

reshaped_img = image[start:end,start:end,: ]
p = 8
N = 3
hill_curve = HilbertCurve(p,N)



frequencies = []
for i in range(256*256):
    frequency = hill_curve.distance_from_coordinates(np.reshape(reshaped_img,(256*256,3))[i])
    frequencies.append(frequency)
print(frequencies)

sampling_rate = 44100
# data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
# scaled = np.int16(data/np.max(np.abs(data)) * 32767)
frequencies = np.asarray(frequencies)
frequencies = np.interp(frequencies, (frequencies.min(), frequencies.max()), (2000, 20*1000))
write('test.wav', sampling_rate, frequencies)

