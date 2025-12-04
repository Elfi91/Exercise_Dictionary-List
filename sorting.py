'''
Goal: Sort lists and check for element existence.
'''

from typing import List

# Create a list 'prices' containing:
price_list: list[int] = ["45.5", "12.0", "78.3", "23.1", "56.7"]

# Convert string prices to floats
float_price: list[float] = [float(price) for price in price_list]

# Create a sorted copy of the list (using sorted())
sorted_price_list = sorted(float_price)

# Count how many prices are greater than 50
limit = 50
count_greater_than_50 = sum(price > limit for price in float_price)

# Find the minimum and maximum price
minimum_price = min(sorted_price_list)
maximum_price = max(sorted_price_list)

# Print the sorted list and results
print("--- Analysis Results ---")
print(f"Sorted price list: {sorted_price_list}")
print(f"Minimum price: {minimum_price}€\nMaximal price: {maximum_price}")

# Verify if 23.1 is in the list
if 23.1 in sorted_price_list:
    print("Yes, 23.1 is in the list")
else:
    print("No, 23.1 is not in the list")

print(f"The number of prices greater than 50 is: {count_greater_than_50}")