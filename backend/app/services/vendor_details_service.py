from app.models.voucher import VendorDetails
from app.schemas.vender_details import VendorDetailsCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class VendorDetailsService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_vendor_details(self, vendor_details_data: VendorDetailsCreate):
        try:
            vendor_details_create = VendorDetailsCreate(**vendor_details_data)
            new_vendor_details = VendorDetails(**vendor_details_create.model_dump())
            self.db.add(new_vendor_details)
            await self.db.commit()
            await self.db.refresh(new_vendor_details)
            return new_vendor_details
        except Exception as e:
            raise

    async def get_vendor_details(self, vendor_details_id: int):
        try:
            result = await self.db.execute(select(VendorDetails).where(VendorDetails.id == vendor_details_id))
            vendor_details = result.scalar_one_or_none()
            return vendor_details
        except Exception as e:
            raise