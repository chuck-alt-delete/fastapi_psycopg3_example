from psycopg_pool import AsyncConnectionPool
from pydantic import BaseModel
from psycopg.rows import class_row

class MyClass(BaseModel):
    a: int
    b: int

async def my_query(pool: AsyncConnectionPool) :
    async with pool.connection() as conn:
        await conn.set_autocommit(True)
        async with conn.cursor(row_factory=class_row(MyClass)) as cur:
            await cur.execute("SELECT a, b FROM my_collection")
            rows = await cur.fetchall()
            return {"data": rows}