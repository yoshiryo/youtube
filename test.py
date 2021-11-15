import datetime
from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

td1 = str(datetime.timedelta(seconds=0))
td1 = '2012-12-29 ' + td1
td1 = dt.strptime(td1, '%Y-%m-%d %H:%M:%S')

td2 = str(datetime.timedelta(seconds=10000))
td2 = '2012-12-29 ' + td2
td2 = dt.strptime(td2, '%Y-%m-%d %H:%M:%S')

td3 = str(datetime.timedelta(seconds=20000))
td3 = '2012-12-29 ' + td3
td3 = dt.strptime(td3, '%Y-%m-%d %H:%M:%S')
dates = [td1, td2, td3]
y = [1, 2, 1]

fig, ax = plt.subplots()
ax.plot(dates, y)
xfmt = mdates.DateFormatter("%H/%M/%S")
xloc = mdates.HourLocator()
ax.xaxis.set_major_locator(xloc)
ax.xaxis.set_major_formatter(xfmt)
# x軸の範囲
#ax.set_xlim() 
ax.grid(True)
plt.show()
