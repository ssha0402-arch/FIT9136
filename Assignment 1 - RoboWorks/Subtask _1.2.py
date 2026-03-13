inventory = {
    'motor': '$49.99',
    'sensor': '$15.75',
    'frame': '$120.00',
    'cpu': '$85.50'
}

print("-" * 20)
print("Product Inventory:")
print("-" * 20)

for name, price in inventory.items():
    print(f"{name:<10} | {price}")
