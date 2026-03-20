# get_model_cost(model, catalog, models)
# can_build_one(model, inventory, models)
# build_one(model, inventory, catalog, models)
# apply_discount(total)

PRICE_CATALOG = {
    "servo": 38.79,
    "lidar": 245.30,
    "motor": 52.99,
    "sensor": 21.45,
    "gyroscope": 132.88,
    "gearbox": 310.60,
    "regulator": 27.14,
    "controller": 89.53
}

MODELS = {
    "R1": {"servo": 4, "lidar": 6, "motor": 5, "sensor": 4, "gyroscope": 0, "gearbox": 2, "regulator": 2, "controller": 7},
    "R2": {"servo": 7, "lidar": 0, "motor": 4, "sensor": 4, "gyroscope": 0, "gearbox": 6, "regulator": 5, "controller": 5},
    "R3": {"servo": 3, "lidar": 6, "motor": 2, "sensor": 7, "gyroscope": 7, "gearbox": 4, "regulator": 4, "controller": 4},
    "R4": {"servo": 1, "lidar": 6, "motor": 3, "sensor": 6, "gyroscope": 4, "gearbox": 5, "regulator": 2, "controller": 7},
}

inventory = {
    "servo": 42,
    "lidar": 28,
    "motor": 63,
    "sensor": 29,
    "gyroscope": 54,
    "gearbox": 51,
    "regulator": 95,
    "controller": 77
}

def get_model_cost(model, catalog, models):
    model_cost = 0
    part_req = models[model]
    for part_name, part_num in part_req.items():
        #print (part_name,part_num)
        model_cost += float(f"{(catalog[part_name] * part_num):.2f}")
    return (model_cost)

# print(get_model_cost ("R1",PRICE_CATALOG,MODELS))

def can_build_one(model, inventory, models) :
    check_list = []
    part_req = models[model]
    for part_name, part_num in part_req.items():
        if part_num <= inventory[part_name]:
            check_list.append(1)
        else:
            check_list.append(0)
    if 0 in check_list:
        return (False)
    else:
        return (True)
    
# print(can_build_one("R1", inventory, MODELS))

def build_one(model, inventory, catalog, models) :
    check_list = []
    check = True
    part_req = models[model]
    for part_name, part_num in part_req.items():
        if part_num <= inventory[part_name]:
            check_list.append(1)
        else:
            check_list.append(0)
    if 0 in check_list:
        check = False 
        #return ("$"+0.00)
        return (0.00)
    model_cost = 0
    part_req = models[model]
    for part_name, part_num in part_req.items():
        model_cost += float(f"{(catalog[part_name] * part_num):.2f}")
    
    if check:
        for part_name, part_num in part_req.items():
            inventory[part_name] -= part_num
            #cost = float(model_cost)
        #return("$" + str(model_cost))
        return (model_cost)

# print(build_one("R1", inventory, PRICE_CATALOG, MODELS))

def apply_discount(total):
    sale_amount = 0.00
    if total > 1500:
        discount = 0.15
    elif total > 1000:
        discount = 0.10
    elif total > 300:
        discount = 0.05
    else:
        discount = 0.0
    sale_amount = float(f"{(total * (1-discount)):.2f}")
    return (sale_amount)

# print(apply_discount(1023.01))