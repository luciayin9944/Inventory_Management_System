from app import app, inventory
import pytest
from unittest.mock import patch, Mock

# Mocked response data from the OpenFoodFacts API
mock_api_response = {
    "status": 1,
    "product": {
        "barcode": "123456",
        "product_name": "Test Product",
        "brands": "Test Brand",
        "countries": "Testplace",
        "ingredients_text": "Sugar, Water",
        "price": "N/A"
    }
}


@pytest.fixture(autouse=True)
def mock_inventory():
    inventory.clear()

def test_get_inventory():
    inventory.append(mock_api_response["product"])
    assert len(inventory) == 1

@patch("app.requests.get")
def test_add_product(mock_get):  # mock_get is the mock object injected by @patch
    client = app.test_client()

    # Create mock response object whose .json() returns predefined data
    mock_response = Mock()
    mock_response.json.return_value = mock_api_response
    mock_get.return_value = mock_response

    # Send POST request to simulate adding a product
    response = client.post("/inventory", json={"barcode": "123456"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Test Product"



def test_update_product():
    client = app.test_client()
    inventory.append(mock_api_response["product"])
    new_price = "9.99"
    response = client.patch("/inventory/123456", json={"price": new_price})
    assert response.status_code == 200
    data = response.get_json()
    assert data["price"] == new_price


def test_delete_product():
    client = app.test_client()
    inventory.append(mock_api_response["product"])
    response = client.delete("/inventory/123456")
    assert response.status_code == 204
    assert len(inventory) == 0

def test_delete_nonexistent_product():
    client = app.test_client()
    inventory.append(mock_api_response["product"])
    response = client.delete("/inventory/000000")
    assert response.status_code == 404
    data = response.get_json()
    assert data["message"] == "Product not found"