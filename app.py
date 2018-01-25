import book_entry
from flask import Flask, request, make_response
from add_booking_controller import add_booking
from compute_metrics_controller import get_all_metrics
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from json import dumps

app = Flask(__name__)

engine = create_engine('sqlite:///dbs/base.db', echo=True)
book_entry.Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


@app.route('/booking', methods=['POST'])
def post_booking():
    if 'file' not in request.files:
        return make_response("Error, nothing in files", 400)
    file = request.files['file']
    if file.filename == '':
        make_response("Error, No filename", 400)
    if add_booking(file, DBSession):
        return make_response('Done', 200)
    else:
        return make_response('File not standard', 400)


@app.route('/booking', methods=['GET'])
def get_booking():
    values = get_all_metrics(DBSession)
    if values is None:
        return make_response("Error querying base", 500)
    return make_response(dumps(values), 200)


if __name__ == '__main__':
    app.run()
