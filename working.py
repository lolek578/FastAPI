from fastapi import FastAPI, Path

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
def get_item(item_id: int = Path(None, description="the id of the item you view")):
    return inventory[item_id]

#query parameter
@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not Found"}