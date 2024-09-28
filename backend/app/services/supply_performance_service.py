from app.models.voucher import SupplyPerformance
from app.schemas.supply_performance import SupplyPerformanceCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class SupplyPerformanceService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_supply_performance(self, supply_performance_data: dict):
        try:
            # Convert the incoming dict to a Pydantic model
            supply_performance_model = SupplyPerformanceCreate(**supply_performance_data)
            new_supply_performance = SupplyPerformance(**supply_performance_model.dict())  # Use dict() to get field values
            
            self.db.add(new_supply_performance)
            await self.db.commit()
            await self.db.refresh(new_supply_performance)
            return new_supply_performance
        except Exception as e:
            raise

    async def get_supply_performance(self, supply_performance_id: int):
        try:
            result = await self.db.execute(select(SupplyPerformance).where(SupplyPerformance.id == supply_performance_id))
            supply_performance = result.scalar_one_or_none()
            return supply_performance
        except Exception as e:
            raise
