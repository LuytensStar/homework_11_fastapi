from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_, extract

from src.database.models import Contact
from src.schemas import ContactModel,ContactResponse

from datetime import datetime, timedelta
async def get_contacts(skip:int,limit:int,db:Session)->List[ContactResponse]:
    return db.query(Contact).offset(skip).limit(limit).all()

async def get_contact(contact_id:int, db:Session)->ContactResponse:
    return db.query(Contact).filter(Contact.id==contact_id).first()

async def create_contact(body:ContactModel, db:Session)->Contact:
    contact = Contact(name=body.name,surname=body.surname,electronic_mail=body.electronic_mail,
                      phone_number=body.phone_number,birth_date=body.birth_date,
                      additional_info=body.additional_info)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def update_contact(contact_id:int, body:Contact, db:Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.electronic_mail = body.electronic_mail
        contact.phone_number = body.phone_number
        contact.birth_date = body.birth_date
        contact.additional_info = body.additional_info
        db.commit()

    return contact

async def delete_contact(contact_id:int, db:Session):
    contact = db.query(Contact).filter(Contact.id==contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        # db.refresh(contact)

    return contact

async def search_contacts(query: str, db: Session)->List[ContactResponse] | None:
    contacts = db.query(Contact).filter(
        or_(
            Contact.name.ilike(f'%{query}%'),
            Contact.surname.ilike(f'%{query}%'),
            Contact.electronic_mail.ilike(f'%{query}%')
        )
    ).all()
    return contacts

async def get_birthdays(db:Session)->List[ContactResponse]:
    now_time = datetime.now().date()
    future_time = now_time + timedelta(days=7)

    contacts = db.query(Contact).filter(
        extract('month', Contact.birth_date) == now_time.month,
        now_time.day <= extract('day', Contact.birth_date),
        extract('day', Contact.birth_date) <= future_time.day
    ).all()

    return contacts
