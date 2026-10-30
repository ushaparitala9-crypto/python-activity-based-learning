name = input("Enter patient name: ")

print("1. General Patient")
print("2. Emergency Patient")
print("3. ICU Patient")

choice = int(input("Enter patient category: "))
days = int(input("Enter number of days: "))

if choice == 1:
    category = "General Patient"
    bill = days * 1000

elif choice == 2:
    category = "Emergency Patient"
    bill = days * 3000

elif choice == 3:
    category = "ICU Patient"
    bill = days * 5000

else:
    category = "Invalid Category"
    bill = 0

print("\n--- Hospital Bill ---")
print("Patient Name:", name)
print("Patient Category:", category)
print("Number of Days:", days)
print("Total Bill: Rs.", bill)

