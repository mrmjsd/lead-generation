from app.models.voucher import Voucher,Payment,SupplyPerformance,FinancialReporting,AuditTrail,VendorDetails,Item
from app.schemas.voucher import VoucherCreate, VoucherUpdate, VoucherRead 
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

    async def create_voucher_from_json(self, data):
        try:
            # Create voucher entry
            voucher = Voucher(
                voucher_no=data['voucher']['voucher_no'],
                date=data['voucher']['date'],
                prepared_by=data['voucher']['prepared_by'],
                approved_by=data['voucher']['approved_by'],
                authorized_by=data['voucher']['authorized_by'],
                receiver_signature=data['voucher']['receiver_signature'],
                total_amount=data['voucher']['total_amount'],
                in_words=data['voucher']['in_words'],
                expense_category=data['voucher']['expense_category'],
                payment_status=data['voucher']['payment_status'],
                payment_dues=data['voucher']['payment_dues'],
                cash_flow_impact=data['voucher']['cash_flow_impact'],
            )
            self.db.add(voucher)
            self.db.commit()
            self.db.refresh(voucher)

            # Create Payment entry
            payment = Payment(
                voucher_id=voucher.id,
                method=data['voucher']['payment']['method'],
                cheque_no=data['voucher']['payment']['cheque_no'],
                cheque_date=data['voucher']['payment']['cheque_date'],
                bank_name=data['voucher']['payment']['bank_name']
            )
            self.db.add(payment)

            # Create Item entries
            for item_data in data['voucher']['items']:
                item = Item(
                    voucher_id=voucher.id,
                    description=item_data['description'],
                    amount=item_data['amount'],
                    category=item_data.get('category', None)  # Optional category
                )
                self.db.add(item)

            # Create Vendor Details entry
            vendor_details = VendorDetails(
                voucher_id=voucher.id,
                vendor_name=data['voucher']['vendor_details']['vendor_name'],
                vendor_contact=data['voucher']['vendor_details']['vendor_contact'],
                vendor_address=data['voucher']['vendor_details']['vendor_address']
            )
            self.db.add(vendor_details)

            # Create Financial Reporting entry
            financial_reporting = FinancialReporting(
                voucher_id=voucher.id,
                report_period=data['voucher']['financial_reporting']['report_period'],
                report_type=data['voucher']['financial_reporting']['report_type']
            )
            self.db.add(financial_reporting)

            # Create Supply Performance entry
            supply_performance = SupplyPerformance(
                voucher_id=voucher.id,
                performance_metrics=data['voucher']['supply_performance']['performance_metrics']
            )
            self.db.add(supply_performance)

            # Create Audit Trail entry
            audit_trail = AuditTrail(
                voucher_id=voucher.id,
                approver=data['voucher']['audit_trail']['approver'],
                preparer=data['voucher']['audit_trail']['preparer'],
                audit_date=data['voucher']['audit_trail']['audit_date']
            )
            self.db.add(audit_trail)

            # Commit all changes to the database
            self.db.commit()

            return voucher
        except Exception as e:
            logger.error(f"Error creating voucher from JSON: {e}")
            raise
