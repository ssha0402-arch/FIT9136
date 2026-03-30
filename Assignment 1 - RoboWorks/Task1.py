
# set origional list
product_name = ["motor", "sensor", "frame", "cpu"]
product_price = [49.99, 15.75, 120.00, 85.50]
product_num = []


# add number into list
print("Welcome to the RoboWorks Quote Calculator.\n\nFor each product below, please specify your required quantity.\n")
for name in product_name:
    num = int(input(name + ": "))
    product_num.append(num)


# calculate total amount
total_amount = 0    
for i in range(len(product_name)):
    total_amount += product_price[i] * product_num[i]

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


# print product name with price
print("\nPlease see your quote below.\n")
for i in range(len(product_name)):
    print(f"{product_name[i]}: {product_num[i]} x ${product_price[i]:.2f} = ${product_price[i] * product_num[i]:.2f}")


print("\nSubtotal: $"+str(f"{total_amount:.2f}"))
print("Discount: $"+str(f"{discount_amount:.2f}"))
print("Total: $"+str(f"{sale_price:.2f}"))