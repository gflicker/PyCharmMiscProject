#Listing an order and what to print on the receipt
print("Please write the items you want to buy")
Groceries = [] #Empty list that we're going to put items we want to buy
while len(Groceries) < 4:
    grocery = input("Write your item: ")
    Groceries.append(grocery)
for things in Groceries:
    Groceries.sort()
print(Groceries)
print("Please call again. Thank you!")