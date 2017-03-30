import numpy as np
import matplotlib.pyplot as plt

num_files = 16

files = []
times = []
for i in range(0,num_files):
	file_size = float(raw_input())
	time = float(raw_input())
	files.append(file_size)
	times.append(time)
files = np.array(files)
times = np.array(times)
plt.plot(files,times,'ro-')
plt.title("Time vs File Size")
plt.xlabel("File Size (bytes)")
plt.ylabel("Time (sec)")
plt.xscale('log')
plt.yscale('log')
plt.show()
