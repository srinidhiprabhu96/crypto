import numpy as np

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
plt.show()
