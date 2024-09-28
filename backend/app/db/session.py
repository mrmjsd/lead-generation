from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = "mysql+aiomysql://root:mrmjpatra@localhost/fastapi_db"

# Create the async engine
async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create a session factory
AsyncSessionLocal = sessionmaker( bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
