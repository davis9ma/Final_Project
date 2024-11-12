import numpy as np

file_directory = "C:\\Users\\Macon Davis\\Documents\\GitHub\\engr340-fall2024\\Final Project\\"
file_name = "student-mat.csv"

data = np.loadtxt((file_directory+file_name),delimiter=";", dtype=str, quotechar='"')
main_data_array = np.array(data)

# Put all variables into their own lists
school = main_data_array[1:,0]
sex = main_data_array[1:,1]
age = main_data_array[1:,2]
address = main_data_array[1:,3]
famsize = main_data_array[1:,4]
Pstatus = main_data_array[1:,5]
Medu = main_data_array[1:,6]
Fedu = main_data_array[1:7]
Mjob = main_data_array[1:8]
Fjob = main_data_array[1:9]
reason = main_data_array[1:10]
guardian = main_data_array[1:11]
traveltime = main_data_array[1:12]
studytime = main_data_array[1:13]
failures = main_data_array[1:14]
schoolsup = main_data_array[1:15]
famsup = main_data_array[1:16]
paid = main_data_array[1:17]
activities = main_data_array[1:18]
nursery = main_data_array[1:19]
higher = main_data_array[1:20]
internet = main_data_array[1:21]
romantic = main_data_array[1:22]
famrel = main_data_array[1:23]
freetime = main_data_array[1:24]
goout = main_data_array[1:25]
Dalc = main_data_array[1:26]
Walc = main_data_array[1:27]
health = main_data_array[1:28]
absences = main_data_array[1:29]
G1 = main_data_array[1:30]
G2 = main_data_array[1:31]
G3 = main_data_array[1:32]

