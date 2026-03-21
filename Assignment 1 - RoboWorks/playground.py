# orgain data

part_name = ["servo", "lidar", "motor", "sensor", "gyroscope", "gearbox", "regulator", "controller"]
part_stock = [42, 28, 63, 29, 54, 51, 95, 77]
part_cost = [38.79, 245.30, 52.99, 21.45, 132.88, 310.60, 27.14, 89.53]

# model data
# models_R1 = [4, 6, 5, 4, 0, 2, 2, 7]
# models_R2 = [7, 0, 4, 4, 0, 6, 5, 5]
# models_R3 = [3, 6, 2, 7, 7, 4, 4, 4]
# models_R4 = [1, 6, 3, 6, 4, 5, 2, 7]

# dict for model
models = {
    "R1": [4, 6, 5, 4, 0, 2, 2, 7],
    "R2": [7, 0, 4, 4, 0, 6, 5, 5],
    "R3": [3, 6, 2, 7, 7, 4, 4, 4],
    "R4": [1, 6, 3, 6, 4, 5, 2, 7]
}

# fix test 2.10
seq_model = []
for model in models.keys():
    seq_model.append(model)

model_cost_amount = {
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0
}


# calculate model cost
for model, req in models.items():
    model_cost = 0
    i = 0                                   # set counter
    while i < len(part_name):
        model_cost += req[i] * part_cost[i]
        i += 1
    model_cost_amount[model] = f"{model_cost:.2f}" # set float to 2

#list for order
queue = [
    ("R4",2),
    ("R1",2),
    ("R3",1),
    ("R2",4),
    ("R1",1),
    ("R4",2),
    ("R2",3)
]
avl_order = []
unavl_order = []

# a new way from task3

for order in queue:
    model_name = order[0]
    model_num = order[1]
    consed_num = 0 
    unconsed_num = 0
    part_req = models[model_name]
    try_num = int(model_num)
    print(order)
    while try_num != 0:
        temp_stock = part_stock.copy()
        check = 1
        model_cost = 0
        i = 0
        while i < len(part_req):
            if temp_stock[i] >= part_req[i] * try_num:
                temp_stock[i] -= part_req[i] * try_num
                model_cost += part_cost[i] * part_req[i] * try_num
                i +=1
                check = 1
            else:
                temp_stock = part_stock.copy()
                check = 0
                model_cost = 0
                break
        if check == 1:
            consed_num = int(try_num)
            unconsed_num = int(model_num) - int(try_num)
            avl_order.append((model_name, consed_num))      # update available order with consed_num
            unavl_order.append((model_name, unconsed_num)) # update unavailable order with remaining number
            part_stock = temp_stock.copy()

            break
        elif check == 0 :
            try_num -=1
            


    if try_num == 0:
        unavl_order.append((model_name, model_num))


    model_cost = float(f"{model_cost:.2f}")