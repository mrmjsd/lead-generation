
from fastapi import APIRouter, Depends, HTTPException
from app.utils.invoice_processor import InvoiceProcessor
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db


router = APIRouter()

@router.get("/pdfparser/", response_model=None)  # No response model
async def create_voucher(db: AsyncSession = Depends(get_db)):
    invoice_processor=InvoiceProcessor('invoice_1.pdf',db)
    response=await invoice_processor.parse_pdf()
    return response