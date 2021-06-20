from fastapi import FastAPI

app = FastAPI()

# the key is product id, value is product
inventory = {
    1: {
        "name": "milk",
        "price": 3.99,
        "brand": "Regular"
    },

    2: {
        "name": "chocolate",
        "price": 5.00,
        "brand": "Schogetten"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
