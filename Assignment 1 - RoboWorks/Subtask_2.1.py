# set origional list
part_name  = ["motor", "sensor", "frame", "cpu"]
part_stock = [5, 7, 10, 2]
part_cost  = [30.50, 10.20, 60.00, 45.95]

#set counter
i = 0 

#print name and price amount
while i < len(part_name):
    price = 0
    price = part_cost[i] * part_stock[i]
    print (part_name[i]+ ": $"+str(f"{price:.2f}"))
    i += 1