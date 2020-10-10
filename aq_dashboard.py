from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aq_dash.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)


api = openaq.OpenAQ()
status, body = api.measurements(city='Los Angeles', parameter='pm25', limit=100)


@APP.route('/')
def root():
    """Base view."""
    return 'TODO'


def get_data(i):
    """Returns list of data to be used"""
    data_list = body['results'][i]
    return data_list


def find_datetime():
    """"""


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<Datetime {}, Value {}>'.format(self.datetime, self.value)


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO
    DB.session.add(request)
    DB.session.commit()
    return 'Data refreshed!'




