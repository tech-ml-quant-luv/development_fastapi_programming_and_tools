from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome BITCH!"

#When we declare other function parameters that are not the part of the path parameters, they are automatically interpreted as "query" parameters.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int=0, limit: int=10):
    return fake_items_db[skip: skip+limit]
#The requested url will become http://127.0.0.1:8000/items/?skip=0&limit=10
# As skip and limit are part of the URL, they are "naturally" strings. But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

# As query parameters are not a fixed part of a path, they can be optional and can have default values.

@app.get("/items/test/{item_id}")
async def read_items(item_id: str, q:int | None= None):
    if q:
        return {"item_id": item_id, "q": fake_items_db[q]}
    return {"item_id": item_id}

# @app.get("/items/req/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item