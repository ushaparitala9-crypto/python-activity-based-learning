budget = float(input("Enter travel budget in INR: "))

print("1. US Dollar (USD)")
print("2. Euro (EUR)")
print("3. British Pound (GBP)")

choice = int(input("Choose currency: "))
amount = float(input("Enter travel expense: "))

if choice == 1:
    expense = amount * 88
    currency = "USD"
elif choice == 2:
    expense = amount * 102
    currency = "EUR"
elif choice == 3:
    expense = amount * 118
    currency = "GBP"
else:
    expense = 0
    currency = "Invalid"

remaining = budget - expense

print("\n--- Travel Budget Analysis ---")
print("Currency:", currency)
print("Travel Expense: Rs.", expense)
print("Total Budget: Rs.", budget)
print("Remaining Budget: Rs.", remaining)

if remaining >= 0:
    print("Status: Within Budget")
else:
    print("Status: Over Budget")

