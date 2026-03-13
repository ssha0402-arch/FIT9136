print("Welcome to the RoboWorks Quote Calculator.\n\nFor each product below, please specify your required quantity.\n")
price_motor = 49.99
price_sensor = 15.75
price_frame = 120.00
price_cpu = 85.50

num_motor = float(input("motor: "))
num_sensor = float(input("sensor: "))
num_frame = float(input("frame: "))  
num_cpu = float(input("cpu: "))

print("\nPlease see your quote below.\n")

total_motor = price_motor * num_motor
total_sensor = price_sensor * num_sensor
total_frame = price_frame * num_frame
total_cpu = price_cpu * num_cpu
total_amount = total_motor + total_sensor + total_frame + total_cpu

if total_amount > 1500:
    discount = 0.15
elif total_amount > 1000:
    discount = 0.10
elif total_amount > 300:
    discount = 0.05
else:
    discount = 0.0
sale_price = total_amount * (1 - discount)
discount_amount = total_amount * discount

print("motor:",str(int(num_motor)),"x $"+str(price_motor),"= $"+str(f"{total_motor:.2f}"))
print("sensor:",str(int(num_sensor)),"x $"+str(price_sensor),"= $"+str(f"{total_sensor:.2f}"))
print("frame:",str(int(num_frame)),"x $"+str(price_frame),"= $"+str(f"{total_frame:.2f}"))
print("cpu:",str(int(num_cpu)),"x $"+str(price_cpu),"= $"+str(f"{total_cpu:.2f}"))

print("\nSubtotal: $"+str(f"{total_amount:.2f}"))
print("Discount: $"+str(f"{discount_amount:.2f}"))
print("Total: $"+str(f"{sale_price:.2f}"))