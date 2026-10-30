product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: "))
cost = float(input("Enter cost per product: "))
selling_price = float(input("Enter selling price per product: "))

total_cost = quantity * cost
total_sales = quantity * selling_price
profit = total_sales - total_cost

print("\n--- Manufacturing Analysis ---")
print("Product Name:", product)
print("Quantity Produced:", quantity)
print("Total Cost: Rs.", total_cost)
print("Total Sales: Rs.", total_sales)
print("Profit: Rs.", profit)

if profit > 0:
    print("Status: Profit")
elif profit < 0:
    print("Status: Loss")
else:
    print("Status: No Profit No Loss")

