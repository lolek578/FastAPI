from fastapi import FastAPI

app = FastAPI()


# create endpoints
@app.get("/")
def home():
    return {"message": "Hello world!"}


@app.get("/about")
def about():
    return {"Data": "About"}
