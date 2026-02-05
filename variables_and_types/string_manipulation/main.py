# Challenge_1 Solution

# Given string
grocery_items = "milk, eggs, cheese, bread, apples"

# Use string slicing to extract the items
dairy1 = grocery_items[0:4]      # "milk"
dairy2 = grocery_items[12:18]    # "cheese"
bakery1 = grocery_items[20:25]   # "bread"

# Build the message using concatenation
message = "We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5"

# Print the result
print(message)