from scipy.signal import butter, filtfilt #filtfilt may help in filtering the phase shifts, have used it in ECG signals before for phase distortion
import numpy as np
import matplotlib.pyplot as plt

signal = np.loadtxt('/Users/shlokp7/Documents/GitHub/Vascular/ASsignment1/PythonTesting/share/signal.txt')
print(signal)

signal_first_half, signal_second_half = np.split(signal, 2) #numpy split function 
print(signal_first_half)
print("")
print(signal_second_half)

#low-pass filter w order 2 and cutoff frequency 10
def butter_low_pass(signal, cutoff=10, fs=100, order=2):
    nyquist = fs / 2 #frequency is half of the og sampling rate
    b, a = butter(order, cutoff/nyquist, btype='low') #butterworth filter based on parameters
    return filtfilt(b, a, signal) #filfilt to mitigate phase distortion 

#high-pass filter w order 4 and cutoff frequency 3
def butter_high_pass(signal, cutoff=3, fs=100, order=4):
    nyquist = fs / 2 #frequency is half of the og sampling rate
    b, a = butter(order, cutoff/nyquist, btype='high') #butterworth filter based on parameters
    return filtfilt(b, a, signal) #filfilt to mitigate phase distortion 

filtered_first_half = butter_low_pass(signal_first_half) #call functions
filtered_second_half = butter_high_pass(signal_second_half)

combined_signal = np.concatenate((filtered_first_half, filtered_second_half)) #combine filtered halves

plt.plot(combined_signal)
plt.title('Stitched Signal using Butterworth Highpass & Lowpass')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.show()

#-------------------Saving the output-------------------

import os

output_dir = '/Users/shlokp7/Documents/GitHub/Vascular/ASsignment1/PythonTesting/output'
os.makedirs(output_dir, exist_ok=True)

plt.plot(combined_signal)
plt.title('Stitched Signal using Butterworth Highpass & Lowpass')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.savefig(os.path.join(output_dir, 'stitched_signal.png'))  
plt.show()

np.savetxt(os.path.join(output_dir, 'stitched_signal.txt'), combined_signal)