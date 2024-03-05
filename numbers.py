import matplotlib.pyplot as plt

numbers = [0.5, 0.6, 6, 1.9, 2, 4, 5.5, 6, 8, 9]

plt.hist(numbers, bins=3)

plt.xlabel("Number")

plt.ylabel("Frequency")

plt.show()
