import uvicorn

from fastapi import FastAPI

from api.v1.api import api_router
from core.config import settings
from db.base import Base
from db.base import engine


Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


