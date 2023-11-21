from fastapi import FastAPI
from icecream import install
install()
from src.routes import get_routers

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    return {"Hello": "World"}

# include routers
for router in get_routers():
    app.include_router(router)
