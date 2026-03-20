###############################
# Place your data model here. #
###############################

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

################################
# Place your API methods here. #
################################

def get_model_cost(model, catalog, models):
    model_cost = 0
    part_req = models[model]
    for part_name, part_num in part_req.items():
        #print (part_name,part_num)
        model_cost += float(f"{(catalog[part_name] * part_num):.2f}")
    return (model_cost)

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

def apply_discount(total):
    sale_amount = 0.00
    total = float(total)
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

def process_order(model, count, inventory, catalog, models):
    temp_stock = inventory         # set a temp list
    consed_num = 0 
    unconsed_num = 0
    try_num = int(count)
    part_req = models[model]
    while try_num != 0:
        check = 1
        # model_cost = 0
        for part_req_name , part_req_num in part_req.items():
            if temp_stock[part_req_name] >= part_req[part_req_name] * try_num:
                temp_stock[part_req_name] -= part_req[part_req_name] * try_num
                # model_cost += catalog[part_req_name] * try_num
                check = 1
            else:
                check = 0
                # model_cost = 0
                break
        if check == 1:
            consed_num = try_num
            unconsed_num = int(count) - int(try_num)
            break
        elif check == 0 :
            try_num -=1
            check = 1
    # model_cost = f"{model_cost:.2f}"
    # model_cost = f"{(get_model_cost(model, catalog, models) * try_num):.2f}"
    model_cost = get_model_cost(model, catalog, models) * try_num
    return (consed_num,unconsed_num,model_cost)

# print (process_order("R1", 7, inventory, PRICE_CATALOG, MODELS))




########################################
# Place your CLI code and methods here #
########################################


while True:
    temp_inventory = inventory # set a temp catalog
    print ("1) Show models and costs\n2) Attempt order\n3) Show inventory\n0) Exit\n")
    choice = input ("Please enter an integer between (0-3): ")

    if str(choice) == str(1):
        # print("11111")
        for model_name, model_req in MODELS.items():
            print(model_name + ": $" + str(f"{get_model_cost(model_name, PRICE_CATALOG, MODELS):.2f}"))
        print("")

    elif str(choice) == str(2):
        model_name = input("Please enter a model number: ")
        hint = "Please enter the number of " + model_name + " units you would like: "
        count = input(hint)
        cons_result = process_order(model_name, count, temp_inventory, PRICE_CATALOG, MODELS)
        discount = apply_discount(cons_result[2])
        print ("\nAttempting to order models...\n\n" + model_name + " order details.")
        print ("Units built: " + str(cons_result[0]))
        print ("Units on backorder: " + str(cons_result[1]))
        print ("\nSubtotal: $" + str(f"{cons_result[2]:.2f}"))
        print ("Discount (dollars): $" + str(f"{(float(cons_result[2])-discount):.2f}"))
        print ("Total: $" + str(discount)+"\n")

    elif str(choice) == str(3):   
        print ("Current inventory:\n")
        for part_name, part_num in temp_inventory.items():
            print (part_name + ": " + str(part_num))
        print("")

    elif str(choice) == str(0):
        break


    