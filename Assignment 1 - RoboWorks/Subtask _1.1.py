price = 52.99
print ("Welcome to the motor line item test script.\n\nMotor price: $"+str(price))
num = float(input("\nHow many motors would you like to buy: "))
# total = round(price * float(num)+0.001,2) #it seems like round() has some problem

total = round(price * float(num),3)
check = str(total)[-1]
if int(check) >= 5:
    total = round(price * float(num)+0.001,2)
else:
    round(price * float(num),2)
# a better round() for subtask_1.1

print ("Total price: $"+str(total))