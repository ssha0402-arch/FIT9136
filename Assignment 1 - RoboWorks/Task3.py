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
    """ return the cost of "model" by the request from "models" and price from "catalog" """
    model_cost = 0
    part_req = models[model]
    for part_name, part_num in part_req.items():
        model_cost += float(f"{(catalog[part_name] * part_num):.2f}")
    return (model_cost)

def can_build_one(model, inventory, models) :
    """ return True if the stock of parts in "inventory" is able to build "model", 
        or False if unable"""
    check_list = []                                 # list of flag to record if a part is able
    part_req = models[model]
    for part_name, part_num in part_req.items():
        if part_num <= inventory[part_name]:
            check_list.append(1)                    # mark as able
        else:
            check_list.append(0)                    # mark as unable
    if 0 in check_list:                             # if any part marked unable
        return (False)                              
    else:
        return (True)
    
def build_one(model, inventory, catalog, models) :
    """ if parts in "inventory" are able to build a "model", update "inventory" and return cost, 
        if unable return 0.00 """
    check_list = []                                 # list of flag to record if a part is able
    part_req = models[model]
    for part_name, part_num in part_req.items():
        if part_num <= inventory[part_name]:
            check_list.append(1)                    # mark as able
        else:
            check_list.append(0)                    # mark as unable
    if 0 in check_list:                             # if any part marked unable 
        return (0.00)
    
    # if avriable to build
    model_cost = 0                                  
    part_req = models[model]
    for part_name, part_num in part_req.items():
        model_cost += float(f"{(catalog[part_name] * part_num):.2f}")
        inventory[part_name] -= part_num                                # update inventory
    return (model_cost)

def apply_discount(total):
    """ return the price after discounted """
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
    """ try to built "model" as more as possible, 
        update "inventory", 
        return the number of built unit, the number of unit on backorder, and total cost"""
    consed_num = 0 
    unconsed_num = 0
    try_num = int(count)
    part_req = models[model]
    check = True                            # mark of if_can_build_or_not
    while check:
        temp_stock = inventory.copy()           # set a temp 
        model_cost = 0
        for part_req_name , part_req_num in part_req.items():
            if temp_stock[part_req_name] >= part_req[part_req_name] * try_num:
                temp_stock[part_req_name] -= part_req[part_req_name] * try_num
                model_cost += catalog[part_req_name] * part_req_num * try_num
                check = True                        # mark as able
            else:
                check = False                       # mark as unable
                model_cost = 0
                break
        if check :                              # check if can build
            consed_num = try_num
            unconsed_num = int(count) - int(try_num)
            inventory.update(temp_stock)        # update inventory
            break
        else :                       
            try_num -=1                         # try partial 
            check = True
    model_cost = float(f"{model_cost:.2f}")
    return (consed_num,unconsed_num,model_cost)


########################################
# Place your CLI code and methods here #
########################################


while True:                                                                                                 # keep working

    print ("1) Show models and costs\n2) Attempt order\n3) Show inventory\n0) Exit\n")                      # menu
    choice = input ("Please enter an integer between (0-3): ")

    if str(choice) == str(1):                                                                               # Show models and costs
        for model_name, model_req in MODELS.items():
            print(model_name + ": $" + str(f"{get_model_cost(model_name, PRICE_CATALOG, MODELS):.2f}"))
        print("")

    elif str(choice) == str(2):                                                                             # Attempt order
        model_name = input("Please enter a model number: ")
        count = input("Please enter the number of " + model_name + " units you would like: ")
        cons_result = process_order(model_name, count, inventory, PRICE_CATALOG, MODELS)
        discount = apply_discount(cons_result[2])
        print ("\nAttempting to order models...\n\n" + model_name + " order details.")
        print ("Units built: " + str(cons_result[0]))
        print ("Units on backorder: " + str(cons_result[1]))
        print ("\nSubtotal: $" + str(f"{cons_result[2]:.2f}"))
        print ("Discount (dollars): $" + str(f"{(float(cons_result[2])-discount):.2f}"))
        print ("Total: $" + str(discount)+"\n")

    elif str(choice) == str(3):                                                                             # Show inventory
        print ("Current inventory:\n")
        for part_name, part_num in inventory.items():
            print (part_name + ": " + str(part_num))
        print("")

    elif str(choice) == str(0):                                                                             # exit
        break                                                                                               


    