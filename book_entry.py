from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BookEntry(Base):
    __tablename__ = 'book_entries'

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer)
    booking_id = Column(String)
    booking_date = Column(DateTime)
    booking_hour = Column(DateTime)
    show_key = Column(Integer)
    show_name = Column(String)
    repr_key = Column(Integer)
    repr_name = Column(String)
    repr_date = Column(DateTime)
    repr_hour = Column(DateTime)
    repr_date_end = Column(DateTime)
    repr_hour_end = Column(DateTime)
    price = Column(Integer)
    product_type = Column(String)
    seller = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String)
    address = Column(String)
    zip_code = Column(Integer)
    country = Column(String)
    age = Column(Integer)
    sex = Column(String)

