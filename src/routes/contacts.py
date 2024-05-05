from typing import List, Union
from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Contact
from src.repository import contacts as repository_contacts
from src.schemas import ContactModel,ContactResponse

router = APIRouter(prefix='/contacts', tags=['contacts'])

@router.get('/', response_model=List[ContactResponse])
async def get_contacts(skip: int=0 , limit:int =100, db: Session=Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip,limit,db)
    return contacts

@router.get('/{contact_id}', response_model=ContactResponse)
async def get_contact(contact_id :int, db: Session=Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id,db)
    if contact is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return contact

@router.post('/', response_model=ContactResponse)
async def create_contact(body:ContactModel, db: Session=Depends(get_db)):
    return await repository_contacts.create_contact(body,db)

@router.put('/{contact_id}', response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.delete('/{contact_id}', response_model=ContactResponse)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id,db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get('/search/',response_model=List[ContactResponse])
async def search_contacts(query:str, db: Session=Depends(get_db)):
    contacts = await repository_contacts.search_contacts(query,db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no contacts with such regex')
    return contacts

@router.get('/birthdays/', response_model= List[ContactResponse])
async def get_birthdays(db: Session=Depends(get_db)):
    contacts = await repository_contacts.get_birthdays(db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no contacts with such birthday')
    return contacts