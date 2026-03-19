# data from task 2


# part_name = ["servo", "lidar", "motor", "sensor", "gyroscope", "gearbox", "regulator", "controller"]
# part_stock = [42, 28, 63, 29, 54, 51, 95, 77]
# part_cost = [38.79, 245.30, 52.99, 21.45, 132.88, 310.60, 27.14, 89.53]
# models_R1 = [4, 6, 5, 4, 0, 2, 2, 7]
# models_R2 = [7, 0, 4, 4, 0, 6, 5, 5]
# models_R3 = [3, 6, 2, 7, 7, 4, 4, 4]
# models_R4 = [1, 6, 3, 6, 4, 5, 2, 7]


# dict requered 

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
# MODELS = {
#     "R1": [4, 6, 5, 4, 0, 2, 2, 7],
#     "R2": [7, 0, 4, 4, 0, 6, 5, 5],
#     "R3": [3, 6, 2, 7, 7, 4, 4, 4],
#     "R4": [1, 6, 3, 6, 4, 5, 2, 7]
# }
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

# calculate model cost
for model_name , req in MODELS.items():
    model_cost = 0 
    for req_name in req.keys():
        model_cost += req[req_name] * PRICE_CATALOG[req_name]
    print (model_name + ": $" + f"{model_cost:.2f}")


# for model, req in MODELS.items():
#     model_cost = 0 
#     i = 0
#     while i < len(req):
#         model_cost += list(req.values())[i] * list(PRICE_CATALOG.values())[i]
#         i+= 1
#     print (model + ": $" + f"{model_cost:.2f}")

# for model, req in MODELS.items():
#     i = 0 
#     model_cost = 0
#     while i < len(req):
#         model_cost += req[i] * list(PRICE_CATALOG.values())[i]      # use list() to trans dict to list 
#         i += 1
#     print (model + ": $" + str(f"{model_cost:.2f}"))                # format 2 float