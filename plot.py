import sys
import pandas as pd
import matplotlib.pyplot as plt

time_begin = 14.3
time_end = 14.8

df = pd.read_csv(sys.stdin, names=['unixtime', 'value'])
plt.figure(figsize=(8, 4))
plt.plot(df['unixtime'],1-df['value'], marker='.')
plt.xlabel('Time (sec)')
plt.ylabel('Eye Openness')
plt.xlim(time_begin, time_end)
plt.ylim(0, 1)
from matplotlib.ticker import MultipleLocator
plt.gca().xaxis.set_major_locator(MultipleLocator(0.1))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))
plt.grid(True)
plt.minorticks_on()
plt.grid(True, which='major', linestyle='--', linewidth=0.6, alpha=0.7)
plt.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.5)

plt.show()
