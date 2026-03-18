# set origional list
part_name  = ["motor", "sensor", "frame", "cpu"]
part_stock = [5, 7, 10, 0]
model = [3, 2, 3, 1]
check = []

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
    print("False")
else:
    print("True")