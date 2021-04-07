import matplotlib.pyplot as plt

f = open('UniformDst.txt')
array = [float(x) for x in f.read().split('\n')[:-1]]

plt.hist(array, bins=100, range=[50, 150])
plt.xlabel('Values in the set')
plt.ylabel('Frequency of occurance')
plt.show()
