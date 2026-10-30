name = input("Enter student name: ")
marks = float(input("Enter percentage of marks: "))
income = float(input("Enter family annual income: "))

print("\n--- Scholarship Details ---")
print("Student Name:", name)

if marks >= 90 and income <= 200000:
    print("Scholarship: 100%")
    print("Status: Eligible")

elif marks >= 80 and income <= 300000:
    print("Scholarship: 75%")
    print("Status: Eligible")

elif marks >= 70 and income <= 500000:
    print("Scholarship: 50%")
    print("Status: Eligible")

else:
    print("Scholarship: Not Available")
    print("Status: Not Eligible")

