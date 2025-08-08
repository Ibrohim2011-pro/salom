from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import Users

app = FastAPI()

@app.get("/")
async def get_users():
    x = await Users.all().values()  # JSON-friendly format
    return {"data": x}

@app.get("/add")
async def add_user(fullname: str, age: int, email: str, password: str):
    user = await Users.create(
        fullname=fullname,
        age=age,
        email=email,
        password=password
    )
    if user:
        return {"status": "success"}
    return {"status": "error"}

register_tortoise(
    app,
    modules={"models": ["models"]},
    db_url="sqlite://users.db",
    generate_schemas=True
)
