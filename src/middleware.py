import time
from main import app
from fastapi import Request


@app.middleware('http')
async def get_process_time(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    print("\n---------------> Process Time :", process_time , "<---------------\n")
    return response