# Inventory_Management_System


A simple yet robust inventory management system for small retail businesses. This system provides a Flask-based REST API for managing inventory items and a command-line interface (CLI) to interact with the API. It also integrates with the OpenFoodFacts API to fetch real-time product details by barcode or product name.

## Features
• ✅ CRUD operations for managing inventory items (Add, View, Update, Delete)  
• 🔎 Fetch product details from OpenFoodFacts API using barcode  
• 🖥️ RESTful API built with Flask  
• 🧑‍💻 Command-Line Interface (CLI) to interact with the system

## Installation
    # Clone the repository
    git clone https://github.com/luciayin9944/Inventory_Management_System.git
    cd Inventory_Management_System

    # Set up virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Run the Flask server
    python app.py


## CLI Usage
#Example CLI commands:

    # Add item by barcode (details fetched automatically)
    python main.py add 3274080005003           
    python main.py add 4311527561858  
    
    # List all inventory items
    python main.py list 
    
    # Update item price by barcode
    python main.py update 3274080005003 3.99
    
    # Delete an item
    python main.py delete 4311527561858 
