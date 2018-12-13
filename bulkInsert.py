import datetime
from sqlalchemy.orm import Session
from Model import Client, FeatureRequest
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = Session(bind=engine)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)


clients = [
  Client(ClientName='Client A'),
  Client(ClientName='Client B'),
  Client(ClientName='Client C'),
]

feature_requests = [
  FeatureRequest(Title="Sample 1", Description="Sample 1 description", TargetDate=tomorrow, 
                ClientPriority=1,ProductArea='Policies', ClientID=1),
  FeatureRequest(Title="Sample 2", Description="Sample 2 description", TargetDate=tomorrow, 
                ClientPriority=2,ProductArea='Policies', ClientID=1),
  FeatureRequest(Title="Sample 3", Description="Sample 3 description", TargetDate=tomorrow, 
                ClientPriority=3,ProductArea='Policies', ClientID=1),
  FeatureRequest(Title="Sample 1", Description="Sample 1 description", TargetDate=tomorrow, 
                ClientPriority=1,ProductArea='Policies', ClientID=2),
  FeatureRequest(Title="Sample 2", Description="Sample 2 description", TargetDate=tomorrow, 
                ClientPriority=2,ProductArea='Policies', ClientID=2),
  FeatureRequest(Title="Sample 3", Description="Sample 3 description", TargetDate=tomorrow, 
                ClientPriority=3,ProductArea='Policies', ClientID=2),
  FeatureRequest(Title="Sample 1", Description="Sample 1 description", TargetDate=tomorrow, 
                ClientPriority=1,ProductArea='Policies', ClientID=3),
  FeatureRequest(Title="Sample 2", Description="Sample 2 description", TargetDate=tomorrow, 
                ClientPriority=2,ProductArea='Policies', ClientID=3),
  FeatureRequest(Title="Sample 3", Description="Sample 3 description", TargetDate=tomorrow, 
                ClientPriority=3,ProductArea='Policies', ClientID=3),
]

session.bulk_save_objects(clients)
session.bulk_save_objects(feature_requests)
session.commit()