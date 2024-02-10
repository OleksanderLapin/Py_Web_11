from datetime import datetime, timedelta
from models.contact import ContactDB
from schemas.contact import ContactUpdate

class ContactRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all(self) -> list[ContactDB]:
        return self.db.query(ContactDB).filter()

    def create(self, contact_item):
        new_contact = ContactDB(**contact_item.dict())
        self.db.add(new_contact)
        self.db.commit()
        self.db.refresh(new_contact)
        return new_contact

    def get_by_id(self, id, name, surname,email):
        if name:
            return self.db.query(ContactDB).filter(ContactDB.name==name).first()
        elif surname:
            return self.db.query(ContactDB).filter(ContactDB.surname==surname).first()
        elif email:
            return self.db.query(ContactDB).filter(ContactDB.email==email).first()
        elif id:
            return self.db.query(ContactDB).filter(ContactDB.id==id).first()

    def up_contact(self, id: int, update_contact: ContactUpdate):
        contact = self.db.query(ContactDB).filter(ContactDB.id == id).first()
        print(contact)
        print(update_contact)
        if contact:
            contact.name = update_contact.name
            contact.surname = update_contact.surname
            contact.email = update_contact.email
            contact.phone = update_contact.phone
            contact.birthday = update_contact.birthday
        self.db.commit()
        return contact
    
    def delete_by_id(self, id: int):
        contact_item = self.db.query(ContactDB).filter(ContactDB.id==id).first()
        if contact_item:
            self.db.delete(contact_item)
            self.db.commit()
        return contact_item

    def get_birthdays(self) -> list[ContactDB]:
        today = datetime.now().date()
        end_date = today + timedelta(days=7)
        return self.db.query(ContactDB).filter((ContactDB.birthday >= today) & (ContactDB.birthday <= end_date))
        
