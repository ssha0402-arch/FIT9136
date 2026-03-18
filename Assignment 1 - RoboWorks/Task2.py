part_name = ["servo", "lidar", "motor", "sensor", "gyroscope", "gearbox", "regulator", "controller"]
part_stock = [42, 28, 63, 29, 54, 51, 95, 77]
part_cost = [38.79, 245.30, 52.99, 21.45, 132.88, 310.60, 27.14, 89.53]

models = {
    "R1": [4, 6, 5, 4, 0, 2, 2, 7],
    "R2": [7, 0, 4, 4, 0, 6, 5, 5],
    "R3": [3, 6, 2, 7, 7, 4, 4, 4],
    "R4": [1, 6, 3, 6, 4, 5, 2, 7]
}

queue = [
    ("R4", 2),
    ("R1", 2),
    ("R3", 1),
    ("R2", 4),
    ("R1", 1),
    ("R4", 2),
    ("R2", 3)
]

model_cost = {
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0
}

for model_name, requirements in models.items():
    i = 0
    while i < len(part_name):
        model_cost[model_name] += requirements[i] * part_cost[i]
        i += 1

constructed_units = {
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0
}

backorder_units = {
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0
}

total_cost = 0

for order in queue:
    model_name = order[0]
    quantity = order[1]
    requirements = models[model_name]
    built = 0

    while built < quantity:
        feasible = True
        i = 0

        while i < len(part_name):
            if part_stock[i] < requirements[i]:
                feasible = False
                break
            i += 1

        if feasible:
            i = 0
            while i < len(part_name):
                part_stock[i] -= requirements[i]
                i += 1
            constructed_units[model_name] += 1
            total_cost += model_cost[model_name]
        else:
            backorder_units[model_name] += 1

        built += 1

print("Constructed units")
for model_name, quantity in constructed_units.items():
    print(model_name + ": " + str(quantity))

print()
print("Total cost: $" + f"{total_cost:.2f}")
print()
print("Backorder")
for model_name, quantity in backorder_units.items():
    print(model_name + ": " + str(quantity))

print()
print("Inventory")
i = 0
while i < len(part_name):
    print(part_name[i] + ": " + str(part_stock[i]))
    i += 1
