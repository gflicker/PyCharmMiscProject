import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/zambia.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, highs, lows, elevations = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = row[7]
        low = row[8]
        elev = row[4]

        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        elevations.append(elev)

    # Plot the high temperatures and shading an area in the chart
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)  # first argument always x-axis, if single argument y-axis only
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.plot(dates, elevations, color='green', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    title = "Zambia's Highs, Lows and Elevation -- 2025-2026"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (C)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
