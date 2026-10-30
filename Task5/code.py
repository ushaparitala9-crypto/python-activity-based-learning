print("1. Basic Plan - Rs. 199")
print("2. Standard Plan - Rs. 399")
print("3. Premium Plan - Rs. 599")

usage = int(input("Enter monthly data usage in GB: "))

if usage <= 5:
    plan = "Basic Plan"
    cost = 199

elif usage <= 15:
    plan = "Standard Plan"
    cost = 399

else:
    plan = "Premium Plan"
    cost = 599

print("\n--- Best Plan Details ---")
print("Selected Plan:", plan)
print("Monthly Usage:", usage, "GB")
print("Total Cost: Rs.", cost)

