import csv
from datetime import datetime

import matplotlib.pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    #Get dates and highs temperature from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

#Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates, highs, color='red') #first argument always x-axis, if single argument y-axis only

#Format plot.
plt.title('Daily hig temperatures, July 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()