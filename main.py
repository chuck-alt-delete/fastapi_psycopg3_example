from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool
from psycopg import conninfo
import uvicorn

from my_config import config
from my_queries import my_query

app = FastAPI()

@app.on_event("startup")
def open_pool(config=config):
    """create database connection pool"""
    app.state.pool = AsyncConnectionPool(
        conninfo = conninfo.make_conninfo(
            user = config["MZ_USER"],
            dbname = config["MZ_DB"],
            host = config["MZ_HOST"],
            password = config["MZ_PASSWORD"],
            port = 6875,
            sslmode = 'require',
            application_name = 'FastAPI',
            options = config["options"],
        ),
        max_size = 500,
        min_size = 5
    )

@app.on_event("shutdown")
async def close_pool():
    """close database connection pool"""
    await app.state.pool.close()

@app.get("/my_data/")
async def get_my_data():
    return await my_query(app.state.pool)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)