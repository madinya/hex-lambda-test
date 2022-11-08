from fastapi import APIRouter

index = APIRouter()


@index.get("/")
async def get():
    return {"message": "Hello world"}
