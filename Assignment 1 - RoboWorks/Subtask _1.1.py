price = 52.99
print ("Welcome to the motor line item test script.\n\nMotor price: $"+str(price))
num = float(input("\nHow many motors would you like to buy: "))
total = round(price * float(num)+0.001,2) #it seems like round() has some problem
print ("Total price: $"+str(total))