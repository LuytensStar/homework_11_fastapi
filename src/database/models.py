from sqlalchemy import Integer,Column,String,func
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    electronic_mail = Column(String(100),nullable=False)
    phone_number = Column(String(20), nullable=False)
    birth_date = Column(Date, default=func.now())
    additional_info = Column(String)
