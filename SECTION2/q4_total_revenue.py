def calculate_total_revenue(sales):
    total = 0
    for item in sales:
        total += item['price'] * item['quantity']
    return total

# Example usage
sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]
print(calculate_total_revenue(sales_data))  # Output: 1260