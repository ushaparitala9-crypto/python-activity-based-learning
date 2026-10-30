event = input("Enter event name: ")

budget = float(input("Enter total budget: "))
food = float(input("Enter food expenses: "))
decoration = float(input("Enter decoration expenses: "))
sound = float(input("Enter sound system expenses: "))
other = float(input("Enter other expenses: "))

total_expenses = food + decoration + sound + other
remaining = budget - total_expenses

print("\n--- Campus Event Financial Report ---")
print("Event Name:", event)
print("Total Budget: Rs.", budget)
print("Total Expenses: Rs.", total_expenses)
print("Remaining Amount: Rs.", remaining)

if remaining > 0:
    print("Status: Budget Saved")
elif remaining < 0:
    print("Status: Budget Exceeded")
else:
    print("Status: Budget Fully Used")

