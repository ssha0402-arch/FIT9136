print ("Welcome to the discount calculator.\n")

sale_amount = float(input("Enter sales amount(dollars):"))

if sale_amount > 1500:
    discount = 0.15
elif sale_amount > 1000:
    discount = 0.10
elif sale_amount > 300:
    discount = 0.05
else:
    discount = 0.0
final_price = sale_amount * (1 - discount)



print("Discounted price: $"+str(f"{final_price:.2f})"))