from fastapi import FastAPI

app = FastAPI()


# create endpoint
@app.get("/")
def home():
    return {"message": "Hello world!"}
