from collections import OrderedDict
ordered_items = OrderedDict()
n = int(input())
name_price = []
for _ in range(n):
    name_price.append(input())
    
for item in name_price:
    items = item.split()
    item_name = ' '.join(items[:-1])
    item_price = int(items[-1])
    if item_name in ordered_items:
        ordered_items[item_name] += item_price
    else:
        ordered_items[item_name] = item_price

for name,price in ordered_items.items():
    print(name, price)
