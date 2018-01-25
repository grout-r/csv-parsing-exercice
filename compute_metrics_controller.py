from book_entry import BookEntry
from sqlalchemy.sql import func


def get_nb_booking(session):
    return session.query(BookEntry).filter().count()


def get_unique_buyer(session):
    return session.query(BookEntry).distinct(BookEntry.email).group_by(BookEntry.email).count()


def get_avg_age(session):
    return session.query(func.avg(BookEntry.age)).filter(BookEntry.age.isnot('')).first()[0]


def get_avg_price_repr(session):
    return session.query(BookEntry.repr_name, func.avg(BookEntry.price)).group_by(BookEntry.repr_name).all()


def get_avg_customer_price(session):
    return session.query(BookEntry.email, func.avg(BookEntry.price)).group_by(BookEntry.email).all()


def get_all_metrics(d_b_session):
    session = d_b_session()
    try:
        values = {
            "nb_booking": get_nb_booking(session),
            "unique_buyer": get_unique_buyer(session),
            "avg_age": get_avg_age(session),
            "avg_price_repr": get_avg_price_repr(session),
            "avg_customer_price": get_avg_customer_price(session)
        }

        return values
    finally:
        session.close()
