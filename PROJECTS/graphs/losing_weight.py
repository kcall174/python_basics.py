# python3
from matplotlib import pyplot as plt

# Data sets -- I used my weight here for an example.
months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June']
weight = [210, 204, 190, 192, 186, 182]

# First Plot
plt.title('Losing Weight Overtime')
plt.xlabel('Months')
plt.ylabel('Weight in lbs')
# plt.show(months, weight) -- if we want a basic version
plt.plot(months, weight, color='red', marker='o', linestyle=':')
plt.show()
