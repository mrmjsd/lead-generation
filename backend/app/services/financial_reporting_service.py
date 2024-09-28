from app.models.voucher import FinancialReporting
from app.schemas.financial_reporting import FinancialReportingCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class FinancialReportingService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_financial_reporting(self, financial_reporting_data: dict):
        try:
            # Convert the incoming dict to a Pydantic model
            financial_reporting_model = FinancialReportingCreate(**financial_reporting_data)
            new_financial_reporting = FinancialReporting(**financial_reporting_model.dict())  # Use dict() to get field values

            self.db.add(new_financial_reporting)
            await self.db.commit()
            await self.db.refresh(new_financial_reporting)
            return new_financial_reporting
        except Exception as e:
            raise

    async def get_financial_reporting(self, financial_reporting_id: int):
        try:
            result = await self.db.execute(select(FinancialReporting).where(FinancialReporting.id == financial_reporting_id))
            financial_reporting = result.scalar_one_or_none()
            return financial_reporting
        except Exception as e:
            raise