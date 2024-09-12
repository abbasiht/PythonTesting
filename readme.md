# Step 0
Please clone the GitHub repo on your computer and ensure your Python environment is set up to use the libraries: NumPy, SciPy, and Matplotlib.

# Step 1
In the shared folder, you will find a signal file named signal.txt. Using the numpy library, open this file as a NumPy array.

# Step 2
Once you have opened it as a NumPy array, split the signal in half and save each half as a separate variable.

# Step 3
Build two functions using the SciPy library:

The first function will take a NumPy array, apply a low-pass Butterworth filter (order=2, cutoff frequency=10 Hz), and output the filtered NumPy array.
The second function will take a NumPy array, apply a high-pass Butterworth filter (order=4, cutoff frequency=3 Hz), and output the filtered NumPy array.

Note the original sampling rate is 100 Hz. 

# Step 4
Apply the low-pass filter to the first half of the signal and the high-pass filter to the second half.

# Step 5
Stitch the two filtered halves back together.

# Step 6
Using Matplotlib, plot the stitched signal and save it as a .png file in the output folder.
Also save the stitched signal as a .txt file in the same folder

# Step 7
Please commit your results to the github.
