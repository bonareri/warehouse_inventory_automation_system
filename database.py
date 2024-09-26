import sqlite3

# Connect to the SQLite database
def connect_db():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('inventory.db')

# General function to execute SQL queries
def execute_query(query, params=()):
    """Execute an SQL query with optional parameters."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

# Create products table 
def create_tables():
    """Create products table in the database."""
    query = '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price TEXT,
            quantity INTEGER,
            category TEXT
        )
    '''
    execute_query(query)

# Add a new product to the database
def add_product(name, price, quantity, category):
    """Insert a new product into the products table."""
    query = 'INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)'
    execute_query(query, (name, price, quantity, category))

if __name__ == "__main__":
    create_tables()
    
    