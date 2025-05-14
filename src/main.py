import uvicorn
from fastapi import FastAPI
from .configurations.database import Base, engine
from .routers.user_route import router as user_router
from .routers.auth_route import router as auth_router




app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="""
### 📘 Project Overview

This API provides a complete system for user registration, authentication, and role-based management using FastAPI and SQLAlchemy.

#### 🔐 Authentication
- Register new users
- Login with JWT-based authentication

#### 👥 User Management
- View and update user profiles
- Admin functionalities to enable/disable users
- Superadmin controls to promote/demote or delete users

#### 🛡 Roles
- **User**: Basic access to their own data
- **Admin**: Manage users
- **Superadmin**: Full access including role control and deletion

""",
    swagger_ui_parameters={"operationsSorter": "method"}
)

app.include_router(user_router)
app.include_router(auth_router)


@app.on_event("startup")    
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


from fastapi import Request
import time

@app.middleware('http')
async def get_process_time(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    print("\n---------------> Process Time :", process_time , "<---------------\n")
    return response

def main():
    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    main()