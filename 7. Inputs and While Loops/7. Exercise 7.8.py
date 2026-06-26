#Making a list and pop it out to another lists
sandwich_orders = ["banana", "pineapple", "apple", "peach", "hamburger"]
finished_orders = []
while sandwich_orders:
    order = sandwich_orders.pop()
    finished_orders.append(order)
    print(f'I have made you a sandwich called {order}')
print("\nHere is a list of all the finished sandwich orders")
for order in finished_orders:
    print(f'\t{order}')
