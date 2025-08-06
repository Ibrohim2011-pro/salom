from fastapi import FastAPI, Request
from  tortoise.contrib.fastapi import register_tortoise
from models import Users

app = FastAPI()

@app.get("/")
async def home():
    x = await Users.all()
    return {"data": x}

@app.get("/add")
async def home(fullname: str, age: int, email: str, password: str):
    try:
        x = await Users.create(fullname=fullname, age=age, email=email, password=password)
        return {"status": "success" }
    except:
        return {"status": "error"} 
    

register_tortoise(app, modules={"models": ["models"]}, db_url="sqlite://users.db")