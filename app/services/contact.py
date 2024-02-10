from fastapi import HTTPException
from repositories.contact import ContactRepository
from schemas.contact import Contact, ContactCreate, ContactUpdate

class ContactService():
    def __init__(self, db) -> None:
        self.repo = ContactRepository(db=db)
        
    def get_all_contacts(self) -> list[Contact]:
        all_contacts_from_db = self.repo.get_all() # list[Contact]
        return [Contact.from_orm(item) for item in all_contacts_from_db]
    
    def create_new(self, contact_item: ContactCreate) -> Contact:
        new_item = self.repo.create(contact_item)
        return Contact.from_orm(new_item)
    
    def get_by_id(self,id: int | None = None, 
                  name: str | None = None,
                  surname: str | None = None,
                  email: str | None = None) -> Contact:
        contact_item = self.repo.get_by_id(id, name, surname,email)
        return contact_item
    
    def up_contact(self, id:int , contact_item: ContactUpdate) -> Contact:
        contact = self.repo.up_contact(id, contact_item)
        return contact

    def delete_contact(self, id:int):
        contact_item = self.repo.delete_by_id(id)
        return contact_item

    def birthdays(self) -> list[Contact]:
        contact_item = self.repo.get_birthdays()
        return [Contact.from_orm(item) for item in contact_item]
