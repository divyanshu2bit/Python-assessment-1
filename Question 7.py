# Program to read purchase data and calculate billing details

file = open("purchase-1.txt", "r")
lines = file.readlines()
file.close()

items_dict = {}       # { item_name : price }
discount_per_item = 0

for line in lines:
    line = line.strip()
    if line == "":
        continue

    if line.startswith("Discount"):
        parts = line.split()
        discount_per_item = int(parts[1])
    else:
        name, price = line.split()
        items_dict[name] = int(price)

# Calculations
num_items = len(items_dict)

# Assume every 3rd item is free
num_free_items = num_items // 3

amount_to_pay = sum(items_dict.values())
discount_given = num_items * discount_per_item
final_amount = amount_to_pay - discount_given

# Display results
print("No of items purchased:", num
