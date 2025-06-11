from pathlib import Path

from fastapi import Depends, FastAPI
from sqlalchemy.sql import text
from uvicorn import run as server_start

from core.db.dependencies.db_helper import db_helper
from core.logger.logger import get_configure_logger

app = FastAPI()

logger = get_configure_logger(Path(__file__).stem)


@app.get("/user/{user_id}")
async def get_user(user_id: int, session=Depends(db_helper.session_dependency)):
    async with session as conn:
        logger.info("Get user %s", user_id)
        result = await conn.execute(text("SELECT 1"))
        result2 = await conn.execute(text("SELECT 2"))
    return result.mappings().fetchone(), result2.mappings().fetchone()


if __name__ == "__main__":
    server_start("main:app", reload=True, host="0.0.0.0", port=8000)
