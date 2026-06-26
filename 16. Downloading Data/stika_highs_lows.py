import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    #Get dates and highs temperature from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#Plot the high temperatures and shading an area in the chart
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5) #first argument always x-axis, if single argument y-axis only
ax.plot(dates, lows, color='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot.
plt.title('Daily high temperatures -- 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()