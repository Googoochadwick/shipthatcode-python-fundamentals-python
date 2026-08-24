item = input()
qty = int(input())
price = float(input())
# Print the 3-line receipt
print(f"Item: {item}")
print(f"Quantity: {qty}")
print(f"Total: ${(price*qty):.2f}")