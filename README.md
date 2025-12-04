# LIST EXERCISES #

## Exercise 1.1: Basic Manipulation
Objective: Familiarize with basic list methods.

Instructions:
- Create a list named servers containing: ["web01", "db01", "cache01"]
- Add "backup01" to the end
- Insert "proxy01" at the beginning (index 0)
- Remove "cache01"
- Print the final list and its length

Expected Output:
['proxy01', 'web01', 'db01', 'backup01']
Number of servers: 4

## Exercise 1.2: Slicing and Access
Objective: Practice element access and slicing.

Instructions:
- Create a list named temperatures containing: [15, 18, 22, 25, 28, 30, 27, 24, 20]
- Print the first temperature
- Print the last temperature
- Print the temperatures from position 2 up to 5 (exclusive)
- Print all temperatures with a step of 2 (skipping one every two)

Expected Output:

First temperature: 15
Last temperature: 20
Temperatures [2:5]: [22, 25, 28]
Every two: [15, 22, 28, 27, 20]

## Exercise 1.3: Sorting and Searching
Objective: Sort lists and check for element existence.

Instructions:
- Create a list named prices containing: [45.5, 12.0, 78.3, 23.1, 56.7]
- Create a sorted copy of the list (using sorted())
- Find the minimum and maximum price
- Check if 23.1 is in the list
- Count how many prices are greater than 50

Expected Output:

Original prices: [45.5, 12.0, 78.3, 23.1, 56.7]
Sorted prices: [12.0, 23.1, 45.5, 56.7, 78.3]
Minimum: 12.0
Maximum: 78.3
23.1 present: True
Prices > 50: 2

# DICTIONARY EXERCISES

## Exercise 2.1: Creation and Access
Objective: Create dictionaries and access values.

Instructions:
- Create a dictionary named config with the following pairs: "host": "192.168.1.1" "port": 8080 "ssl": True "timeout": 30
- Print the value of "host"
- Modify "port" to 443
- Add a new key "protocol" with value "https"
- Print the complete dictionary

Expected Output:

Host: 192.168.1.1
{'host': '192.168.1.1', 'port': 443, 'ssl': True, 'timeout': 30, 'protocol': 'https'}

## Exercise 2.2: Iteration
Objective: Iterate over dictionaries.

Instructions:
- Create a dictionary named users with the following pairs: 
    "alice": "admin" 
    "bob": "user" 
    "charlie": "guest"
- Iterate over the dictionary and print each pair in the format: "Username: alice, Role: admin"
- Check if "bob" is a present key
- Print all keys (usernames)
- Print all values (roles)

Expected Output:

Username: alice, Role: admin
Username: bob, Role: user
Username: charlie, Role: guest
bob present: True
Usernames: dict_keys(['alice', 'bob', 'charlie'])
Roles: dict_values(['admin', 'user', 'guest'])

## Exercise 2.3: Counting Occurrences
Objective: Use dictionaries to count occurrences.

Instructions:
- Create a list named grades containing: ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
- Create an empty dictionary named count
- Iterate over the grades list and count how many times each grade appears in the dictionary
- Print the final dictionary (Hint: Use count.get(grade, 0) to handle missing keys)

Expected Output:

Grade count: {'A': 4, 'B': 3, 'C': 2, 'D': 1}ù

## Exercise 3.1: List of Dictionaries
Objective: Manage a list of dictionaries (similar to a database).

Instructions:
- Create a list named products containing 4 dictionaries, each with keys "name", "price", "quantity": 
    {"name": "Laptop", "price": 899.99, "quantity": 5} 
    {"name": "Mouse", "price": 25.50, "quantity": 50} 
    {"name": "Keyboard", "price": 75.00, "quantity": 30} 
    {"name": "Monitor", "price": 299.99, "quantity": 15}
- Iterate over the list and print only the products with a price greater than 100
- Calculate the total inventory value (price × quantity for each product)

Expected Output:

Products > €100:
- Laptop: €899.99
- Monitor: €299.99

Total inventory value: 12524.80€