from app.models.voucher import Payment
from app.schemas.payment import PaymentCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class PaymentService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_payment(self, payment_data: PaymentCreate):
        try:
            new_payment = Payment(**payment_data)
            self.db.add(new_payment)
            await self.db.commit()
            await self.db.refresh(new_payment)
            return new_payment
        except Exception as e:
            raise

    async def get_payment(self, payment_id: int):
        try:
            result = await self.db.execute(select(Payment).where(Payment.id == payment_id))
            payment = result.scalar_one_or_none()
            return payment
        except Exception as e:
            raise