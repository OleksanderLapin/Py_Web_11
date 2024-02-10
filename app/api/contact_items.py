
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.contact import Contact, ContactCreate, ContactUpdate
from dependencies.database import get_db, SessionLocal
from services.contact import ContactService

router = APIRouter()

@router.get("/list/")
async def list_contacts(db: SessionLocal = Depends(get_db)) -> list[Contact]:
    contact_items = ContactService(db=db).get_all_contacts()
    return contact_items

@router.get("/identify/")
async def get_contact(id:int | None = None,
                      name: str | None = None,
                      surname: str | None = None,
                      email: str | None = None,
                      db: SessionLocal = Depends(get_db)
                      ) -> Contact:
    contact_item = ContactService(db=db).get_by_id(id, name, surname, email)
    if contact_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found")
    return contact_item

@router.post("/create_contact/")
async def create_contact(contact_item: ContactCreate, 
                         db: SessionLocal = Depends(get_db)
                         ) -> Contact:
    new_item = ContactService(db=db).create_new(contact_item)
    return new_item

@router.put("/update/{id}")
async def update_contact(id: int, 
                         contact_update: ContactUpdate, 
                         db: SessionLocal = Depends(get_db)
                         ) -> Contact:
    contact = ContactService(db=db).up_contact(id, contact_update)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found")
    return contact

@router.delete("/delete/{id}")
async def delete_contact(id: int, 
                         db: SessionLocal = Depends(get_db)):
    contact_item = ContactService(db=db).delete_contact(id)
    if contact_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found")
    return contact_item

@router.get("/birthdays/")
async def birthdays(db: SessionLocal = Depends(get_db)) -> list[Contact]:
    contacts = ContactService(db=db).birthdays()
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found")
    return contacts

