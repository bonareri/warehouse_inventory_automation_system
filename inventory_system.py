from database import execute_query 
import csv
from alert import send_email_alert  

# Add a new product to the inventory
def add_products(name, price, quantity, category): 
    query = """
        INSERT INTO products (name, price, quantity, category)
        VALUES (?, ?, ?, ?)
    """
    execute_query(query, (name, price, quantity, category))

# View stock information for all products and store it in a CSV file
def view_all_products():
    query = """ SELECT * FROM products """
    products = execute_query(query).fetchall()

    # Write stock information to a CSV file
    with open('products_stock.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['ID', 'Name', 'Price', 'Quantity', 'Category'])
        # Write the data
        writer.writerows(products)

    print("Product information has been written to products_stock.csv.")
    check_low_stock()  # Check for low stock after viewing products

# Retrieve product information of a single item from the database
def get_product_info(product_id):
    query = """ SELECT * FROM products WHERE id = ? """
    product = execute_query(query, (product_id,)).fetchone()
    return product

# Update stock level of an existing product
def update_stock(product_id, quantity):
    query = """
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    """
    execute_query(query, (quantity, product_id))

# Delete products from the database
def delete_products(product_id):
    query = """
        DELETE FROM products 
        WHERE id = ?
    """
    result = execute_query(query, (product_id,))
    
    if result.rowcount == 0:
        print(f"No product found with ID {product_id}.")
    else:
        print(f"Product with ID {product_id} has been deleted.")

def check_low_stock(threshold=10):
    """Check stock levels for all products and send an alert if below threshold."""
    query = 'SELECT id, name, quantity FROM products'
    products = execute_query(query).fetchall()

    for product in products:
        product_id, name, quantity = product
        if quantity < threshold:
            send_email_alert(name, quantity)  # Send email alert
            print(f"Low stock alert for {name}. Current quantity: {quantity}.")

def main_menu():
    while True:
        print("\nWarehouse Inventory Management System")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product Stock")
        print("4. View Product Info")
        print("5. Delete Product")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = int(input("Enter product quantity: "))
            category = input("Enter product category: ")
            add_products(name, price, quantity, category)
            print(f"Product '{name}' added successfully.")
        
        elif choice == '2':
            view_all_products()
        
        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            quantity = int(input("Enter new quantity: "))
            update_stock(product_id, quantity)
            print(f"Stock for product ID {product_id} updated to {quantity}.")
        
        elif choice == '4':
            product_id = int(input("Enter product ID to view: "))
            product_info = get_product_info(product_id)
            if product_info:
                print(f"Product Info: ID: {product_info[0]}, Name: {product_info[1]}, Price: {product_info[2]}, Quantity: {product_info[3]}, Category: {product_info[4]}")
            else:
                print(f"No product found with ID {product_id}.")
        
        elif choice == '5':
            product_id = int(input("Enter product ID to delete: "))
            delete_products(product_id)
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
