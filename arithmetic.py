# arithmetic.py: Practice arithmetic and formatting
price = 19.99  # float: product price
quantity = 3   # int: number of items
tax_rate = 0.08  # float: 8% tax

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")