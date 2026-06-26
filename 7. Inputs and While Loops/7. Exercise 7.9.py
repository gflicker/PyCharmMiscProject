#Removing duplicates
sandwich_orders = [
    "pastrami", "Peanut Butter", "pastrami", "Smorrebrod",
    "Cheeseburger", "Sharwama", "pastrami"
]
finished = "The deli has run out of pastrami"
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    if "pastrami" not in sandwich_orders:
        print(f'Sorry, {finished}')
print("These are the only sandwich orders remaining.")
for order in sandwich_orders:
    print(f'\t{order}')