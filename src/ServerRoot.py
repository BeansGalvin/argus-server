from fastapi import FastAPI

application = FastAPI()

class ServerRoot():

    @application.get("/")
    async def root():
        return {"message": "Hello World"}

    @application.get("/myPath")
    async def my_path():
        return {"message": "My Path!"}

    @application.get("/Client")
    async def client():
        return {"message": "20"}