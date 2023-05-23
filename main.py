from fastapi import FastAPI, Request
from psycopg_pool import AsyncConnectionPool
import uvicorn

from my_config import MY_DSN_STRING
from my_queries import my_query

app = FastAPI()

@app.on_event("startup")
def open_pool():
    """create database connection pool"""
    app.state.pool = AsyncConnectionPool(MY_DSN_STRING, max_size=500)

@app.on_event("shutdown")
async def close_pool():
    """close database connection pool"""
    await app.state.pool.close()

@app.get("/my_data/")
async def get_my_data():
    return await my_query(app.state.pool)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)