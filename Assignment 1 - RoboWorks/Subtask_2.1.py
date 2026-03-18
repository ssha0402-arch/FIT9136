part_name = ["motor", "sensor", "frame", "cpu"]
part_stock = [5, 7, 10, 2]
part_cost = [30.50, 10.20, 60.00, 45.95]

if __name__ == "__main__":
    i = 0

    while i < len(part_name):
        price = part_cost[i] * part_stock[i]
        print(part_name[i] + ": $" + str(f"{price:.2f}"))
        i += 1
