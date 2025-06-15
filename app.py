import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, jsonify, request


app = Flask(__name__)

inventory = []

def get_product_info(barcode):
    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}.json"
    response = requests.get(url, auth=HTTPBasicAuth('off', 'off'))
    data = response.json()

    if data.get("status") == 1:
        product = data["product"]
        return {
            "barcode": barcode,
            "name": product.get("product_name", ""),
            "brand": product.get("brands", ""),
            "ingredients_text": product.get("ingredients_text", ""),
            "price": product.get("price", "N/A")
        }
    else:
         print("Product not found")
         return None


@app.route("/inventory", methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory", methods=['POST'])
def add_product():
    data = request.get_json()
    barcode = data.get('barcode')

    for item in inventory:
        if item['barcode']== barcode:
            return jsonify({"message": "Product already in inventory"}), 409
        
    new_product = get_product_info(barcode)
    if new_product is None:
        return jsonify({"message": "Product not found"}), 404
    inventory.append(new_product)
    return jsonify(new_product), 201

@app.route("/inventory/<barcode>", methods=['PATCH'])
def update_product(barcode):
    data = request.get_json()
    new_price = data.get('price')

    for product in inventory:
        if product['barcode'] == barcode:
            product['price'] = new_price
            return jsonify(product), 200
        
    return jsonify({"message": "Product not found"}), 404

    
@app.route("/inventory/<barcode>", methods=['DELETE'])
def delete_product(barcode):
    for product in inventory:
        if product['barcode'] == barcode:
            inventory.remove(product)
            return '', 204
        
    return jsonify({"message": "Product not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)