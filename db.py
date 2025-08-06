from tortoise import Tortoise, run_async

async def init():
    await Tortoise.init(
        db_url='sqlite://users.db',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

run_async(init())