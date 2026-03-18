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

model_coast = {
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
    model_coast[model] = f"{model_cost:.2f}" # set float to 2

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

for order in queue: 
    model_name = order[0]           # KEY
    model_num = order[1]
    model_req = models[model_name]  # LIST
    temp_stock = part_stock         # set a temp list
    consed_num = 0 
    i = 0                           # set counter
    while i < len(model_req):                           # try to constrct full order
        check = 1
        if part_stock[i] >= model_req[i] * model_num:
            check = 1
            i += 1
        else:
            check = 0
            i = 0
            break
    if check == 1:
        consed_num = model_num
    else:                                               # try to construct partial order
        try_num = model_num - 1
        while try_num > 0:
            check = 1
            i = 0
            while i < len(model_req):
                if part_stock[i] >= model_req[i] * try_num:
                    check = 1
                    i += 1
                else:
                    check = 0
                    i = 0
                    break
            if check == 1:
                consed_num = try_num
                i = 0
                break
            else:
                try_num -= 1
    if consed_num >= 1:
        i = 0
        while i < len(model_req):
            part_stock[i] -= model_req[i] * consed_num  # fix test 2.5
            i += 1
#        part_stock = temp_stock                         # fix test 2.5
        avl_order.append((model_name, consed_num))      # update available order with consed_num
        unavl_order.append((model_name, model_num - consed_num)) # update unavailable order with remaining number
    else:
#        temp_stock = part_stock                         # fix test 2.5
        unavl_order.append((order))                     # update unavailable order



# for order in queue:
#     i= 0                            # set counter
#     consed_num = 0                  # set conter for constrcted number
#     temp_stock = part_stock         # set a temp list
#     model_name = order[0]           
#     model_num = order[1]            
#     model_req = models[model_name]  
#     while i < len(model_req) :
#         if part_stock[i] >= model_req[i] * model_num:   # try to constrct full order
#             temp_stock[i] -= model_req[i] * model_num
#             i += 1
#             consed_num += model_num
#         else:                                           # try to construct partial order
#             try_num = model_num -1
#             while try_num > 0:
#                 if part_stock[i] >= model_req[i] * try_num:
#                     temp_stock[i] -= model_req[i] * try_num
#                     i += 1
#                     consed_num += try_num
#                     break
#                 else:
#                     try_num -= 1
#             i += 1
#     if consed_num >= 1:
#         part_stock = temp_stock     # update stock
#         avl_order.append(order)     # update available order
#     else:
#         temp_stock = []             # reset temp stock
#         unavl_order.append(order)   # update unavailable order


# dict for consumption unit
cons_unit = {}
for model in seq_model:
    cons_unit[model] = 0
# fix test 2.10

for order in avl_order:
    model_name = order[0]
    model_num = order[1]
    cons_unit[model_name] += model_num

# dict for unconsumption unit
uncons_unit = {}
for model in seq_model:
    uncons_unit[model] = 0
# fix test 2.10

for order in unavl_order:
    model_name = order[0]
    model_num = order[1]
    uncons_unit[model_name] += model_num


# calculate total cost
total_cost = 0
i = 0 # reset counter
for model, model_num in cons_unit.items():
    for model_name, model_cost in model_coast.items():
        if model == model_name:
            total_cost += float(model_cost) * model_num





# temp check
# print("Available orders:", avl_order)    
# print("Unavailable orders:", unavl_order)
# print("Remaining stock:", part_stock)
# print("Model cost:", model_coast)
# print("Total cost:", total_cost)



print ("Constructed units")
for model, model_num in cons_unit.items():
    print( model +":" , str(int(model_num)))

print ("\nTotal cost: $"+ f"{total_cost:.2f}"+"\n\nBackorder") #format total cost float to 2

for model, model_num in uncons_unit.items():
    print( model+ ": "+ f"{model_num}" )


print("\nInventory")

i = 0 # reset counter
while i < len(part_name):
    print(part_name[i] + ": " + str(part_stock[i]))
    i += 1
