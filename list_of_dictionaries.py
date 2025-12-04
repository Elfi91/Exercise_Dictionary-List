'''
Goal: Manage a list of dictionaries (similar to a database).
'''

# Create a 'products' list containing 4 dictionaries, each with keys "name", "price", "quantity":
products: list[dict] = [
    {"name": "Laptop", "price": 899.99, "quantity": 5},
    {"name": "Mouse", "price": 25.50, "quantity": 50},
    {"name": "Tastiera", "price": 75.00, "quantity": 30},
    {"name": "Monitor", "price": 299.99, "quantity": 15}
]

# Iterate over the list and print only the products with a price greater than 100
print("--- Prodcut with price > 100€ ---")
for product in products:
    if product["price"] > 100:
        # If the condition is TRUE, print the entire dictionary
        print(f"{product['name']} : {product['price']}")


# Calculate the total inventory value (price × quantity for each product)
total_inventory_value: float = 0.0

for product in products:
    partial_value = product["price"] * product["quantity"]
    
    total_inventory_value += partial_value

# Stampa il risultato finale
print(f"Valore totale dell'inventario: {total_inventory_value:.2f}€")
