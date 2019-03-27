import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2014.csv'

# Get high temperatures from file.
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  dates, highs, lows = [], [], []
  for row in reader:
    try:
      current_date = datetime.strptime(row[0], "%Y-%m-%d")
      low = int(row[3])
      high = int(row[1])
    except ValueError:
      print(current_date, "Missing data (low or high temperature)")
    else:
      dates.append(current_date)
      highs.append(high)
      lows.append(low)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # draws the labels diagonally to prevent overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
