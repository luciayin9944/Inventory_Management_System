import argparse
import requests

API_URL = "http://localhost:5000/inventory"

def list_inventory(args=None):
    response = requests.get(API_URL)
    print(response.status_code)
    if response.status_code == 200:
        for item in response.json():
            print(item)

    else:
        print("Failed to fetch inventory")


def add_item(args):
    barcode = args.barcode
    response = requests.post(API_URL, json={"barcode": barcode})
    if response.status_code == 201:
        print("Product added:", response.json())
    elif response.status_code == 409:
        print("Product already exists.")
    else:
        print(" Failed to add product.")

def update_item(args):
    barcode = args.barcode
    price = float(args.price)

    response = requests.patch(f"{API_URL}/{barcode}", json={"price": price})
    if response.status_code == 200:
        print("Price updated:", response.json())
    else:
        print("Update failed:")

def delete_item(args):
    barcode = args.barcode
    response = requests.delete(API_URL, json={"barcode": barcode})
    if response.status_code == 204:
        print("Product deleted:", barcode)
    else:
        print("Delete failed:")



def main():
    parser = argparse.ArgumentParser(description="Inventory Managment CLI")
    subparsers = parser.add_subparsers()

    #Add project
    add_parser = subparsers.add_parser("add", help="Add a new product")
    add_parser.add_argument("barcode", help="product's barcode")
    add_parser.set_defaults(func=add_item)

    #List inventory
    list_parser = subparsers.add_parser("list", help="List products in inventory")
    list_parser.set_defaults(func=list_inventory)

    #Update project's price
    update_parser = subparsers.add_parser("update", help="Update price of project")
    update_parser.add_argument("barcode", help="product's barcode")
    update_parser.add_argument("price", help="product's price")
    update_parser.set_defaults(func=update_item)

    #Delete project
    delete_parser = subparsers.add_parser("delete", help="Delete a product")
    delete_parser.add_argument("barcode", help="product's barcode")
    delete_parser.set_defaults(func=delete_item)

    # Parse arguments
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

    
