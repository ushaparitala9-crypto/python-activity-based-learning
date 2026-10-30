name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

final_bill = amount - discount

print("\n--- Retail Bill ---")
print("Customer Name:", name)
print("Purchase Amount: Rs.", amount)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_bill)

