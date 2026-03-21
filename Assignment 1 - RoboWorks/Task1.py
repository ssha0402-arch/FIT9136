
# set origional list
product_name = ["motor", "sensor", "frame", "cpu"]
product_price = [49.99, 15.75, 120.00, 85.50]
product_num = []

i = 0 #set counter for while loop

print("Welcome to the RoboWorks Quote Calculator.\n\nFor each product below, please specify your required quantity.\n")
#price_motor = 49.99
#price_sensor = 15.75
#price_frame = 120.00
#price_cpu = 85.50
#num_motor = int(input("motor: "))
#num_sensor = int(input("sensor: "))
#num_frame = int(input("frame: "))  
#num_cpu = int(input("cpu: "))

# add number into list
for name in product_name:
    num = int(input(name + ": "))
    product_num.append(num)

#total_motor = price_motor * num_motor
#total_sensor = price_sensor * num_sensor
#total_frame = price_frame * num_frame
#total_cpu = price_cpu * num_cpu
#total_amount = total_motor + total_sensor + total_frame + total_cpu

total_amount = 0    # set origional amount
i = 0               # reset conter
# calculate total amount
while i < len(product_name):
    total_amount += product_price[i] * product_num[i]
    i += 1

# calculate discount
if total_amount > 1500:
    discount = 0.15
elif total_amount > 1000:
    discount = 0.10
elif total_amount > 300:
    discount = 0.05
else:
    discount = 0.0

# calculate sale price and discount 
sale_price = total_amount * (1 - discount)
discount_amount = total_amount * discount

print("\nPlease see your quote below.\n")

#print("motor:",str(int(num_motor)),"x $"+str(price_motor),"= $"+str(f"{total_motor:.2f}"))
#print("sensor:",str(int(num_sensor)),"x $"+str(price_sensor),"= $"+str(f"{total_sensor:.2f}"))
#print("frame:",str(int(num_frame)),"x $"+str(price_frame),"= $"+str(f"{total_frame:.2f}"))
#print("cpu:",str(int(num_cpu)),"x $"+str(price_cpu),"= $"+str(f"{total_cpu:.2f}"))

i = 0               # reset conter
# print product name with price
while i < len(product_name):
    print(f"{product_name[i]}: {product_num[i]} x ${product_price[i]:.2f} = ${product_price[i] * product_num[i]:.2f}")
    i += 1

print("\nSubtotal: $"+str(f"{total_amount:.2f}"))
print("Discount: $"+str(f"{discount_amount:.2f}"))
print("Total: $"+str(f"{sale_price:.2f}"))