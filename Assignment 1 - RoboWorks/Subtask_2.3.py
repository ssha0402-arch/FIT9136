# set origional list
part_name  = ["motor", "sensor", "frame", "cpu"]
part_stock = [5, 7, 10, 2]
part_cost  = [30.50, 10.20, 60.00, 45.95]
model = [3, 2, 3, 1]
check = []
enough = 0

# set counter
i = 0

# check stock
while i < len(part_name):
    if part_stock[i] >= model[i]:
        check.append(1)
    else:
        check.append(0)
    i += 1  

# check if 0 exist
if 0 in check:
    enough = False
else:
    enough = True

#print (enough)

i = 0 # reset counter

if enough:
    price = 0
    while i < len(part_name):
        price += part_cost[i] * model[i]
        part_stock[i] -= model[i]
        i += 1
    print ("The model can be constructed and will cost $"+ str(f"{price:.2f}"))
else:
    print ("The model cannot be constructed.")
