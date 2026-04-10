available_products = {"Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"}
sold_items = {"Mouse", "Webcam"}

still_in_stock = available_products - sold_items

sold_out = available_products.intersection(sold_items)

print(f"Total Catalog:     {available_products}")
print(f"Items Sold:        {sold_out}")
print(f"Current Stock:     {still_in_stock}")