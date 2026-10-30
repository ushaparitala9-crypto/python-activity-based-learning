name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))

print("\n1. Sleeper - Rs. 200")
print("2. AC - Rs. 500")
print("3. First Class - Rs. 1000")

choice = int(input("Enter travel class: "))
tickets = int(input("Enter number of tickets: "))

if choice == 1:
    fare = 200
    category = "Sleeper"
elif choice == 2:
    fare = 500
    category = "AC"
elif choice == 3:
    fare = 1000
    category = "First Class"
else:
    fare = 0
    category = "Invalid Class"

if fare > 0:
    if age < 5:
        total = 0
    elif age >= 60:
        total = fare * tickets * 0.9
    else:
        total = fare * tickets

    print("\n--- Railway Reservation ---")
    print("Passenger Name:", name)
    print("Travel Class:", category)
    print("Number of Tickets:", tickets)
    print("Total Fare: Rs.", total)
else:
    print("Invalid travel class!")

