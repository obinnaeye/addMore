from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


from Model import Client, FeatureRequest
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = Session(bind=engine)

session.query(Client).delete()
session.query(FeatureRequest).delete()
session.execute("ALTER SEQUENCE clients_id_seq RESTART WITH 1")
session.execute("ALTER SEQUENCE featurerequests_id_seq RESTART WITH 1")
session.commit()