#python3



#GROUND SHIPPING VARIABLES
weight = 41.5             #change this number 
ground_cost = 20.00
drone_shipping_cost = 0
premium_ground_cost = 125

print("The cheapest option would total: ")


if weight <= 2:
  ground_cost = weight * 1.50 + ground_cost
elif weight <= 6:
 ground_cost = weight * 3.00 + ground_cost
elif weight <= 10:
  ground_cost = weight * 4.00 + ground_cost
else:
  ground_cost = weight * 4.75+ ground_cost
  print(ground_cost)

  print("Premium Ground Shipping Premium: $", premium_ground_cost)


#DRONE SHIPPING VARIABLES
print("Drone Shipping Cost:")

if weight <= 2:
  drone_cost = weight * 4.50 + drone_shipping_cost
elif weight <= 6:
 drone_cost = weight * 9.00 + drone_shipping_cost
elif weight <= 10:
  drone_cost = weight * 12.00 + drone_shipping_cost
else:
  drone_cost = weight * 14.25+ drone_shipping_cost

print(drone_cost) 
