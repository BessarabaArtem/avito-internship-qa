import pytest
import requests
import random

BASE_URL = "https://qa-internship.avito.com/api/1"
SELLER_ID = random.randint(111111, 999999)

def get_item_id_from_response(response):
    try:
        return response.json().get("status", "").split()[-1]
    except:
        return None

def test_create_item():
    payload = {
        "sellerID": SELLER_ID,
        "name": f"Test Phone {SELLER_ID}",
        "price": 250000,
        # Попытка №2: Пихаем поля прямо в корень, раз сервер такой капризный
        "contacts": 0,
        "likes": 0,
        "viewCount": 0
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    assert response.status_code == 200, f"Response: {response.text}"
    assert "status" in response.json()

def test_get_item_by_id():
    payload = {
        "sellerID": SELLER_ID,
        "name": "MacBook Pro",
        "price": 150000,
        "contacts": 0, "likes": 0, "viewCount": 0
    }
    create_resp = requests.post(f"{BASE_URL}/item", json=payload)
    item_id = get_item_id_from_response(create_resp)
    assert item_id is not None

    response = requests.get(f"{BASE_URL}/item/{item_id}")
    assert response.status_code == 200, f"Response: {response.text}"
    
    data = response.json()[0]
    assert data["sellerId"] == SELLER_ID
    assert data["name"] == payload["name"]

def test_get_seller_items():
    payload = {
        "sellerID": SELLER_ID, 
        "name": "Item", 
        "price": 100,
        "contacts": 0, "likes": 0, "viewCount": 0
    }
    requests.post(f"{BASE_URL}/item", json=payload)
    
    response = requests.get(f"{BASE_URL}/{SELLER_ID}/item")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_statistic():
    payload = {
        "sellerID": SELLER_ID, 
        "name": "Stat Item", 
        "price": 100,
        "contacts": 0, "likes": 0, "viewCount": 0
    }
    create_resp = requests.post(f"{BASE_URL}/item", json=payload)
    item_id = get_item_id_from_response(create_resp)

    response = requests.get(f"{BASE_URL}/statistic/{item_id}")
    assert response.status_code == 200
    
    stats = response.json()[0]
    assert "likes" in stats
    assert "viewCount" in stats
    assert "contacts" in stats

def test_create_item_negative_price():
    payload = {
        "sellerID": SELLER_ID,
        "name": "Bad Price Item",
        "price": -100,
        "contacts": 0, "likes": 0, "viewCount": 0
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    assert response.status_code == 400, f"Bug! Response: {response.status_code}"

def test_get_non_existent_item():
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(f"{BASE_URL}/item/{fake_id}")
    assert response.status_code == 404