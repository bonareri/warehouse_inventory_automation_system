# Warehouse Inventory Management System with Jumia Scraper

A Python-based inventory management system that scrapes product data from **Jumia**, stores it in a **CSV file**, and allows users to manage the inventory. This system can add new products, view existing ones, update stock, and send low-stock alerts via email.

---

## 📌 Features

- ✅ Scrape product data from **Jumia** (name, price, category, and stock information)
- ✅ Store scraped data in a **CSV file**
- ✅ Add, update, and delete products in the database
- ✅ View inventory and export it to a CSV file
- ✅ Automatic **low stock alerts** via email
- ✅ **Search by category** for easier product management
- ✅ Simple **CLI interface** for interacting with the system

---

## 🧠 Technologies Used

| Component        | Technology        |
|------------------|-------------------|
| Language         | Python 3          |
| Web Scraping     | BeautifulSoup, requests |
| Database         | SQLite            |
| File Handling    | CSV module        |
| Email Alerts     | `smtplib`, custom script |

---

## 🗃️ Folder Structure

Warehouse-Inventory/
├── alert.py # Sends low stock email alerts
├── database.py # Handles DB connection and queries
├── inventory_system.py # Main logic for managing inventory
├── inventory.db # SQLite Database with product info
├── jumia.html # Scraped HTML data from Jumia (can be parsed)
├── products_stock.csv # Scraped product data saved as CSV
├── scrapper.py # Scrapes product data from Jumia website
├── .gitignore # Gitignore file to exclude unnecessary files
└── README.md # Project documentation

## 🛠️ How to Run the Project

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/warehouse-inventory.git
cd warehouse-inventory
```


