import json
from fastapi.testclient import TestClient

from main import router

client = TestClient(router)


def test_read_all_items():
    response = client.get("/listing/",headers={})
    assert response.status_code == 200
    assert response.json() == [
  {
    "address": "12r ParkwayDr.",
    "price": 255000,
    "id": 2342423
  },
  {
    "address": "1222 Jones Rd.",
    "price": 135000,
    "id": 3343234
  },
  {
    "address": "33 Main Street",
    "price": 245000,
    "id": 22344324
  },
  {
    "address": "34 Main Street",
    "price": 145000,
    "id": 22344325
  },
  {
    "address": "35 Main Street",
    "price": 255000,
    "id": 22344326
  },
  {
    "address": "36 Main Street",
    "price": 140000,
    "id": 22344327
  },
  {
    "address": "37 Main Street",
    "price": 215000,
    "id": 22344328
  },
  {
    "address": "38 Main Street",
    "price": 225000,
    "id": 22344329
  },
  {
    "address": "39 Main Street",
    "price": 235000,
    "id": 22344330
  }
] 


def test_read_item_bad_id():
    response = client.get("/listing/123", headers={})
    assert response.status_code == 404

def test_read_item_good_id():
    response = client.get("/listing/22344325", headers={})
    assert response.status_code == 200
    assert response.json() == {"id":22344325,"address":"34 Main Street", "price":145000}

def test_update_item_bad_id():
    response = client.patch("/listing/",data=json.dumps({"id":2,"address":"34 Main Street", "price":145000}))
    assert response.status_code == 404

def test_update_item_good_id():
    #pre condition - item should exist
    response = client.get("/listing/22344325", headers={})
    assert response.status_code == 200
    assert response.json() == {"id":22344325,"address":"34 Main Street", "price":145000}

    #update - item
    response = client.patch("/listing/", data=json.dumps({"id":22344325,"address":"334 Main Street", "price":150000}))
    assert response.status_code == 200

    #check db that item updated
    response = client.get("/listing/22344325", headers={})
    assert response.status_code == 200
    assert response.json() == {"id":22344325,"address":"334 Main Street", "price":150000}

def test_delete_item_bad_id():
    response = client.delete("/listing/2", headers={})
    assert response.status_code == 404
    
def test_delete_item_good_id():
    #precond: item should exit on db
    response = client.get("/listing/22344325", headers={})
    assert response.status_code == 200

    #action: delete item
    response = client.delete("/listing/22344325", headers={})
    assert response.status_code == 200

    #postcond: item do not exist in db
    response = client.get("/listing/22344325", headers={})
    assert response.status_code == 404

def test_insert_item_new_id():
    #precond: item do not exist in db
    response = client.get("/listing/22344000",headers={})
    assert response.status_code == 404

    #action: insert item
    response = client.post("/listing/",
        data=json.dumps({"id":22344000,"address":"3 New Street", "price":150000}))
    assert response.status_code == 200

    #postcond: item exist in db  
    response = client.get("/listing/22344000", headers={})
    assert response.status_code == 200
    assert response.json() == {"id":22344000,"address":"3 New Street", "price":150000}

def test_insert_item_dublicate_id():
    #precond: item exist in db
    response = client.get("/listing/22344000", headers={})
    assert response.status_code == 200

    #action: try to insert item, get dublicate key error
    response = client.post("/listing/", headers={},data=json.dumps({"id":22344000,"address":"3 New Street", "price":150000}))
    assert response.status_code == 409