from app.models.voucher import Voucher  # Adjust the import based on your project structure
from app.schemas.voucher import VoucherCreate, VoucherUpdate, VoucherRead  # Adjust imports for your Pydantic models
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import logging
from app.logging_config import LogConfig
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(LogConfig().LOGGER_NAME)

class VoucherService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_voucher(self, voucher_data: VoucherCreate):
        try:
            new_voucher = Voucher(**voucher_data.dict())
            self.db.add(new_voucher)
            await self.db.commit()
            await self.db.refresh(new_voucher)
            logger.info(f"Voucher created with ID: {new_voucher.id}")
            return new_voucher
        except Exception as e:
            logger.error(f"Error creating voucher: {e}")
            raise

    async def get_voucher(self, voucher_id: int):
        try:
            result = await self.db.execute(select(Voucher).where(Voucher.id == voucher_id))
            voucher = result.scalar_one_or_none()
            if voucher:
                logger.info(f"Voucher retrieved with ID: {voucher_id}")
            else:
                logger.warning(f"Voucher with ID {voucher_id} not found")
            return voucher
        except Exception as e:
            logger.error(f"Error retrieving voucher with ID {voucher_id}: {e}")
            raise

    async def get_all_vouchers(self):
        try:
            result = await self.db.execute(select(Voucher))
            vouchers = result.scalars().all()
            logger.info(f"Retrieved {len(vouchers)} vouchers")
            return [VoucherRead.model_validate(voucher) for voucher in vouchers]
        except Exception as e:
            logger.error(f"Error retrieving all vouchers: {e}")
            raise

    async def update_voucher(self, voucher_id: int, voucher_update: VoucherUpdate):
        try:
            db_voucher = await self.get_voucher(voucher_id)
            if not db_voucher:
                logger.warning(f"Voucher with ID {voucher_id} not found for update")
                return None
            for key, value in voucher_update.dict(exclude_unset=True).items():
                setattr(db_voucher, key, value)
            await self.db.commit()
            logger.info(f"Voucher with ID {voucher_id} updated")
            return db_voucher
        except Exception as e:
            logger.error(f"Error updating voucher with ID {voucher_id}: {e}")
            raise

    async def delete_voucher(self, voucher_id: int):
        try:
            db_voucher = await self.get_voucher(voucher_id)
            if db_voucher:
                await self.db.delete(db_voucher)
                await self.db.commit()
                logger.info(f"Voucher with ID {voucher_id} deleted")
                return db_voucher
            else:
                logger.warning(f"Voucher with ID {voucher_id} not found for deletion")
                return None
        except Exception as e:
            logger.error(f"Error deleting voucher with ID {voucher_id}: {e}")
            raise
