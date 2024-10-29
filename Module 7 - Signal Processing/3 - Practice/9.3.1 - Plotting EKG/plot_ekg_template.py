
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import matplotlib_fname


# import the CSV file using numpy
path = "C:\\Users\\Macon Davis\\Documents\\GitHub\\engr340-fall2024\\data\\ekg\\mitdb_100.csv"

# load data in matrix from CSV file; skip first two rows
matrix = np.loadtxt(path,delimiter=",",skiprows=2)


# save each vector as own variable

time = matrix[:,0]
mlii = matrix[:,1]
v5 = matrix[:,2]

# use matplot lib to generate a single

plt.title("EKG Data")
plt.plot(time,v5)
plt.show()