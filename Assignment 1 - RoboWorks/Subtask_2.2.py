# set origional list
part_name  = ["motor", "sensor", "frame", "cpu"]
part_stock = [5, 7, 10, 0]                          #different with 2.1
part_cost  = [30.50, 10.20, 60.00, 45.95]
model = [3, 2, 3, 1]
check = []
enough = 0

# check stock
for i in range(len(part_name)):
    if part_stock[i] >= model[i]:
        check.append(1)
    else:
        check.append(0) 

# check if 0 exist
if 0 in check:
    enough = False
else:
    enough = True

print (enough)