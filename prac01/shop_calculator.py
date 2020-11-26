items = int(input("Number of items: "))
while items < 0:
    items = int(input("Number of items: "))
total = 0
for i in range(items):
    price = int(input("Price of item: "))
    total = total + price
print("Total price for",items,"items is $",total)
