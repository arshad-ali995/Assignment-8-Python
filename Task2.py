# TASK 2: Product Price Manager

# 1. Create a dictionary with 3 products and their prices
products = {"Apple": 100, "Milk": 150, "Bread": 80}

# 2. Print all products with prices
print("Products and Prices:")
for product, price in products.items():
    print(product, ":", price)

# 3. Add one new product
products["Eggs"] = 200
print("After adding Eggs:", products)

# 4. Update price of one product
products["Milk"] = 180
print("After updating Milk price:", products)

# 5. Calculate total price
print("Total Price:", sum(products.values()))