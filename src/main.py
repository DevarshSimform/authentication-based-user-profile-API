import uvicorn
from fastapi import FastAPI
from .configurations.database import Base, engine
from .routers.user_route import router as user_router
from .routers.auth_route import router as auth_router



app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)


@app.on_event("startup")    
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


def main():
    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    main()