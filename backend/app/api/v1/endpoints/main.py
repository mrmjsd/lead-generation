from fastapi import APIRouter
from app.api.v1.endpoints import voucher  # Ensure the correct import path

api_router = APIRouter()
api_router.include_router(voucher.router, tags=["vouchers"])
