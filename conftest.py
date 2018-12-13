from testing.postgresql import Postgresql
import pytest

from app import create_app
from Model import db as _db
from Model import Client, FeatureRequest
db_url = "postgresql://postgres:mat610@localhost/addmoretest"

class TestConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'test'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mat610@localhost/addmoretest"


@pytest.yield_fixture(scope='session')
def app():
    _app = create_app(TestConfig)
    # with Postgresql() as postgresql:
    _app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='session')
def testapp(app):
    return app.test_client()


@pytest.yield_fixture(scope='session')
def db(app):
    _db.app = app
    _db.create_all()

    yield _db



@pytest.fixture(scope='session', autouse=False)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)
    clients = [
      Client(ClientName='Client A'),
      Client(ClientName='Client B'),
      Client(ClientName='Client C'),
    ]

    db.session = session_
    db.session.bulk_save_objects(clients)

    yield session_

    transaction.rollback()
    connection.close()
    session_.remove()

  