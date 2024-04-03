import matplotlib.pyplot as plt

height_ranges = ['135-140', '140-145', '145-150', '150-155']
num_students = [4, 12, 16, 8]

bin_edges = [int(range_.split('-')[0]) for range_ in height_ranges]
bin_edges.append(int(height_ranges[-1].split('-')[1]))

plt.hist(bin_edges[:-1], bins=bin_edges, weights=num_students, color='black', edgecolor='grey')

plt.xlabel('Height')
plt.ylabel('Number of Students')
plt.title('Histogram of Height of Students')

plt.show()
