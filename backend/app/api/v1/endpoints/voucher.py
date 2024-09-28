from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db  # Adjust based on your DB session retrieval method
from app.services.voucher_service import VoucherService
from app.schemas.voucher import VoucherCreate, VoucherUpdate,VoucherRead
from app.utils.invoice_processor import InvoiceProcessor
from app.utils.constant import get_file_uploader_dir
router = APIRouter()

@router.post("/vouchers/", response_model=VoucherCreate)
async def create_voucher(voucher: VoucherCreate,  db: AsyncSession = Depends(get_db)):
    service = VoucherService(db)
    new_voucher=await service.create_voucher(voucher)
    return new_voucher

@router.get("/vouchers/{voucher_id}", response_model=VoucherRead)
async def read_voucher(voucher_id: int, db: AsyncSession = Depends(get_db)):
    service = VoucherService(db)
    voucher =await service.get_voucher(voucher_id)
    if voucher is None:
        raise HTTPException(status_code=404, detail="Voucher not found")
    return voucher

@router.get("/vouchers/", response_model=list[VoucherRead])
async def read_all_vouchers(db: AsyncSession = Depends(get_db)):
    service = VoucherService(db)
    vouchers = await service.get_all_vouchers()  # Await the async service call
    return vouchers  # Return the awaited result

@router.put("/vouchers/{voucher_id}", response_model=VoucherCreate)
async def update_voucher(voucher_id: int, voucher_update: VoucherUpdate, db: AsyncSession = Depends(get_db)):
    service = VoucherService(db)
    updated_voucher =await service.update_voucher(voucher_id, voucher_update)
    if updated_voucher is None:
        raise HTTPException(status_code=404, detail="Voucher not found")
    return updated_voucher

@router.delete("/vouchers/{voucher_id}", response_model=VoucherCreate)
async def delete_voucher(voucher_id: int, db: AsyncSession = Depends(get_db)):
    service = VoucherService(db)
    deleted_voucher =await service.delete_voucher(voucher_id)
    if deleted_voucher is None:
        raise HTTPException(status_code=404, detail="Voucher not found")
    return deleted_voucher

@router.get("/voucher/pdfparser", response_model=VoucherRead)  # No response model
async def create_voucher(db: AsyncSession = Depends(get_db)):
    invoice_processor=InvoiceProcessor('invoice_1.pdf',db)
    response=await invoice_processor.parse_pdf()
    return response

@router.get("/voucher/process-pdfs")  # No response model
async def process_pdfs(db: AsyncSession = Depends(get_db)):
    # Get the upload directory
    upload_dir = get_file_uploader_dir()
    
    # Create a FileProcessor instance
    file_processor = InvoiceProcessor(db)  # Replace with your actual DB instance
    
    # Process the PDF files
    result = await file_processor.process_pdf_files(upload_dir)
    
    return {"message": result}


