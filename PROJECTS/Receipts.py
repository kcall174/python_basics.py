#! python3
#  script.py - this program speeds up the process of reciepts

#Stores namesake
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#Price of loveseat
lovely_loveseat_price = 254.00

#Stylish Sette
stylish_sette_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#Price of Stylish Sette
stylish_sette_price = 180.50

#Lamp decsription
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#Price of Lamp
luxuious_lamp_price = 52.15

#Sales tax 8.8%
sales_tax = 0.88

#First customer purchase
customer_one_total = 0

#Description of customer1 purchase
customer_one_itemization = ""

#Customer1 loveseat purchase
customer_one_total = lovely_loveseat_price 

#Customer1 puchase description
customer_one_itemization = lovely_loveseat_description

#Customer1 lamp purchase
customer_one_total += luxuious_lamp_price

#Customer1 puchase description updated
customer_one_itemization += luxurious_lamp_description

#Customer1 total + sales tax 
customer_one_tax = customer_one_total * sales_tax

#Customer1 total + tax
customer_one_total + customer_one_tax

#Receipt heading
print("Customer One Items:")

#Updated customer_one_itemization
print(customer_one_itemization)

#Receipt heading for total cost
print("Customer One Total:")

#Printing total
print(customer_one_total)



