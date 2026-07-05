import requests

API_KEY = "cbbacc55c18493943292705d"

def get_exchange_rates(base_currency):
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(BASE_URL)
    data = response.json()

    if data["result"] == "success":
        return data["conversion_rates"]
    else:
        return None


def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)

    if rates is None:
        print("Something went wrong fetching rates.")
        return

    if to_currency not in rates:
        print(f"Currency {to_currency} not found.")
        return

    result = amount * rates[to_currency]
    print()
    print("==============================")
    print(f"  {amount} {from_currency} = {result:.2f} {to_currency}")
    print("==============================")


# ── Main program ──────────────────────
running = True
while running:
    print("===== LIVE CURRENCY CONVERTER =====")
    amount = float(input("Enter amount: "))
    from_currency = input("Enter currency FROM (e.g ZMW): ").upper()
    to_currency = input("Enter currency TO (e.g USD): ").upper()

    print(f"\nFetching live rates for {from_currency}...")
    convert_currency(amount, from_currency, to_currency)

    #Stopping the program
    switch = input("'Do you want to convert another amount? (yes/no): ")
    switch = switch.lower()
    if switch != "yes":
        running = False