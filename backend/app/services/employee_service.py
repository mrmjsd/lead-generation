from app.models.voucher import Employee
from app.schemas.employee import EmployeeCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class EmployeeService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_employee(self, employee_data: EmployeeCreate):
        try:
            new_employee = Employee(**employee_data.model_dump())
            self.db.add(new_employee)
            await self.db.commit()
            await self.db.refresh(new_employee)
            return new_employee
        except Exception as e:
            raise

    async def get_employee(self, employee_id: int):
        try:
            result = await self.db.execute(select(Employee).where(Employee.id == employee_id))
            employee = result.scalar_one_or_none()
            return employee
        except Exception as e:
            raise
    async def create_employee_if_not_exists(self,voucher_to_data):
        # Extract name and code from voucher_to
        name = voucher_to_data.get("name")
        code = voucher_to_data.get("code")

        # Check if the employee already exists
        existing_employee = await self.db.execute(
            select(Employee).filter(Employee.code == code)
        )
        existing_employee = existing_employee.scalars().first()

        if existing_employee:
            # Return the existing employee's ID
            return existing_employee.id
        else:
            # Create a new employee
            new_employee = Employee(name=name, code=code)
            self.db.add(new_employee)
            await self.db.commit()  # Commit the transaction
            return new_employee.id