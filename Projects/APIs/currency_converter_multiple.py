# Converting to multiple currencies at once
import json
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

def show_comparison_table(amount, from_currency, target_currencies):
    rates = get_exchange_rates(from_currency)

    if rates is None:
        print("Something went wrong fetching rates.")
        return None

    print()
    print(f"{amount} {from_currency} =")

    results = {}
    for currency in target_currencies:
        if currency in rates:
            converted = amount * rates[currency]
            print(f"  {currency}  →  {converted:,.2f}")
            results[currency] = round(converted, 2)
        else:
            print(f"  {currency}  →  Not found")

    return results

# ── Main program ──────────────────────
running = True
while running:
    print("===== LIVE CURRENCY CONVERTER =====")
    amount = float(input("Enter amount: "))
    from_currency = input("Enter currency FROM (e.g ZMW): ").upper()

    print(f"\nFetching live rates for {from_currency}...")
    currencies = input("Enter the currencies you want to convert: ").upper()
    target_currencies = []
    for currency in currencies.split(","):
        cleaned = currency.strip().upper()
        target_currencies.append(cleaned)

    print(target_currencies)

    show_comparison_table(amount, from_currency, target_currencies)

    # Saving it to a json file
    results = show_comparison_table(amount, from_currency, target_currencies)

    if results:
        filename = 'converted_currencies.json'
        with open(filename, 'w') as jsonfile:
            json.dump(results, jsonfile, indent=2)
        print(f"Saved to: {filename}")

    #Stopping the program
    switch = input("Do you want to convert another amount? (yes/no): ")
    switch = switch.lower()
    if switch != "yes":
        running = False




