#! python3
# stacked.bars.py -- shows 2 different location types stacked on top of eachother and their sales in a nice chart with a legend. 
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(sales1)),
 sales1)
plt.bar(range(len(sales2)),
  sales2,
  bottom=sales1)
plt.legend(['Location 1', 'Location 2'])
plt.show()
