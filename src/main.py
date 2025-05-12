import uvicorn
from fastapi import FastAPI
from .configurations.database import Base, engine

app = FastAPI()


@app.on_event("startup")    
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


def main():
    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    main()