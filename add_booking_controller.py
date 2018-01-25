import csv
from io import TextIOWrapper
from book_entry import BookEntry
from datetime import datetime


def add_booking(file, d_b_session):
    session = d_b_session()
    try:
        decoded_file = TextIOWrapper(file)
        reader = csv.reader(decoded_file, delimiter=';')
        reader.__next__()
        print(BookEntry.__table__)
        for row in reader:
            new_entry = BookEntry(
                ticket_id=row[0],
                booking_id=row[1],
                booking_date=datetime.strptime(row[2], "%d/%m/%y %H:%M"),
                booking_hour=datetime.strptime(row[3], "%H:%M:%S"),
                show_key=row[4],
                show_name=row[5],
                repr_key=row[6],
                repr_name=row[7],
                repr_date=datetime.strptime(row[8], "%d/%m/%y"),
                repr_hour=datetime.strptime(row[9], "%H:%M:%S"),
                repr_date_end=datetime.strptime(row[10], "%d/%m/%y"),
                repr_hour_end=datetime.strptime(row[11], "%H:%M:%S"),
                price=row[12],
                product_type=row[13],
                seller=row[14],
                last_name=row[15],
                first_name=row[16],
                email=row[17],
                address=row[18],
                zip_code=row[19],
                country=row[20],
                age=row[21],
                sex=row[22]
            )
            session.add(new_entry)
        session.commit()
        return True
    except IndexError:
        return False
    finally:
        session.close()
