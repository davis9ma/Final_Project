import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'Macon In Hand 200'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".txt"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.loadtxt(signal_filepath, skiprows=2, delimiter=",")
time=signal[:,0]
mlii=signal[:,1]
v5=signal[:,2]
plt.title('Raw Signal for ' + database_name)
plt.plot(v5)
plt.show()

## YOUR CODE HERE ##

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
v5=np.diff(v5)
plt.title('Diffs Signal for ' + database_name)
plt.plot(v5)
plt.show()

"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
v5= (np.square(v5))
plt.title('Squared Signal for ' + database_name)
plt.plot(v5)
plt.show()
"""
Step 5: Pass a moving filter over your data
"""
window_size=10
ones=(np.ones(window_size) / window_size)
v5= np.convolve(v5,ones)
## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(v5)
plt.show()