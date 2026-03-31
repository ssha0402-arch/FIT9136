# orgain data
part_name = ["servo", "lidar", "motor", "sensor", "gyroscope", "gearbox", "regulator", "controller"]
part_stock = [42, 28, 63, 29, 54, 51, 95, 77]
part_cost = [38.79, 245.30, 52.99, 21.45, 132.88, 310.60, 27.14, 89.53]

# dict for model
models = {
    "R1": [4, 6, 5, 4, 0, 2, 2, 7],
    "R2": [7, 0, 4, 4, 0, 6, 5, 5],
    "R3": [3, 6, 2, 7, 7, 4, 4, 4],
    "R4": [1, 6, 3, 6, 4, 5, 2, 7]
}

# dict to record cost
model_cost_amount = {
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0
}

# calculate model cost
for model, req in models.items():
    model_cost = 0
    for i in range(len(part_name)):
        model_cost += req[i] * part_cost[i]
    model_cost_amount[model] = f"{model_cost:.2f}" 

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
able_order = []
backorder = []

# process order
for order in queue:
    model_name = order[0]
    model_num = order[1]
    consed_num = 0 
    unconsed_num = 0
    try_num = int(model_num)                                        # try to built full order first
    part_req = models[model_name]
    while try_num != 0:
        temp_stock = part_stock.copy()                              # set a temp 
        check = True                                                # mark of if_can_build_or_not
        model_cost = 0
        for i in range(len(part_req)):
            if temp_stock[i] >= part_req[i] * try_num:
                temp_stock[i] -= part_req[i] * try_num
                model_cost += part_cost[i] * part_req[i] * try_num
                check = True                                           # mark as able
            else:
                check = False                                           # mark as unable
                model_cost = 0
                try_num -=1                                         # try to build partial order  
                break
        if check:                                              # if all parts are able
            consed_num = int(try_num)
            unconsed_num = int(model_num) - int(try_num)
            able_order.append((model_name, consed_num))              # update able order with consed_num
            backorder.append((model_name, unconsed_num))          # update unable order with remaining number
            part_stock[:] = temp_stock.copy()                              # update stock
            break
            
    if try_num == 0:                                                # if total not able
        backorder.append((model_name, model_num))



# fix test 2.10
seq_model = []
for model in models.keys():
    seq_model.append(model)

# dict for consumption unit
cons_unit = {}
for model in seq_model:
    cons_unit[model] = 0
for order in able_order:
    model_name = order[0]
    model_num = order[1]
    cons_unit[model_name] += model_num

# dict for unconsumption unit
uncons_unit = {}
for model in seq_model:
    uncons_unit[model] = 0
for order in backorder:
    model_name = order[0]
    model_num = order[1]
    uncons_unit[model_name] += model_num



# calculate total cost
total_cost = 0
for model, model_num in cons_unit.items():
    for model_name, model_cost in model_cost_amount.items():
        if model == model_name:
            total_cost += float(model_cost) * model_num

# temp check
# print("Available orders:", avl_order)    
# print("Unavailable orders:", unavl_order)
# print("Remaining stock:", part_stock)
# print("Model cost:", model_cost_amount)
# print("Total cost:", total_cost)

print ("Constructed units")
for model, model_num in cons_unit.items():
    print( model +":" , str(int(model_num)))

print ("\nTotal cost: $"+ f"{total_cost:.2f}"+"\n\nBackorder") 
for model, model_num in uncons_unit.items():
    print( model+ ": "+ f"{model_num}" )

print("\nInventory")
for i in range(len(part_name)):
    print(part_name[i] + ": " + str(part_stock[i]))
