from distutils.dep_util import newer

import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
### YOUR CODE HERE

filepath = "C:\\Users\\Macon Davis\\Documents\\GitHub\\engr340-fall2024\\data\\drop-jump\\all_participant_data_rsi.csv"
full_dataset = np.loadtxt(filepath, delimiter=",", skiprows=1, dtype=str)
data_array = np.array((full_dataset[:,1:]), dtype=float)

#put each column in a variable
trial = full_dataset[:,0]
force_plate_rsi = data_array[:,0]
accelerometer_rsi = data_array[:,1]
percent_error = data_array[:,2]


"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE

#load each force and acceleration into their own lists
B_Force = force_plate_rsi[0:8]
B_Accel = accelerometer_rsi[0:8]

C_Force = force_plate_rsi[8:17]
C_Accel = accelerometer_rsi[8:17]

D_Force = force_plate_rsi[17:27]
D_Accel = accelerometer_rsi[17:27]

E_Force =
E_Accel =



"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), with the 10th bin encompassing [2,inf). An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE


"""
Force Plate
"""
### YOUR CODE HERE

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE

"""
Question 4 (Bonus): Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE