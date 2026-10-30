name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))

if salary >= 50000:
    tax = salary * 0.10
else:
    tax = salary * 0.05

pf = salary * 0.05
total_deduction = tax + pf
net_salary = salary - total_deduction

print("\n--- Employee Salary Details ---")
print("Employee Name:", name)
print("Basic Salary: Rs.", salary)
print("Tax: Rs.", tax)
print("PF: Rs.", pf)
print("Total Deduction: Rs.", total_deduction)
print("Net Salary: Rs.", net_salary)

