import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) #Reader reads the file given as an argument
    header_row = next(reader) #From what has been read we just get the first line
        # print(header_row)

    # enumerate()creates a number list of all the line that has been ready in the csv file
    # for index, column_header in enumerate(header_row):
        # print(index, column_header)

    """Extracting and Reading data from CSV file"""
    #Get high temperatures from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    # print(highs)
#Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(highs, color='red')

#Format plot.
plt.title('Daily hig temperatures, July 2018', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
