from app.models.voucher import AuditTrail
from app.schemas.audit_trail import AuditTrailCreate
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from app.logging_config import LogConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(LogConfig().LOGGER_NAME)

class AuditTrailService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_audit_trail(self, audit_trail_data: dict):
        try:
            logger.info(f"Creating audit trail with data: {audit_trail_data}")
            audit_trail_model = AuditTrailCreate(**audit_trail_data)  # This will validate the input
            new_audit_trail = AuditTrail(**audit_trail_model.dict())
            self.db.add(new_audit_trail)
            await self.db.commit()
            await self.db.refresh(new_audit_trail)
            return new_audit_trail
        except Exception as e:
            logger.error(f"Error creating audit trail: {e}")
            raise

