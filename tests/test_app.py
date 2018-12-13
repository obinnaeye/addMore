import datetime
import json
from Model import Client, FeatureRequest
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from configTest import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = Session(bind=engine)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)


clients = [
  Client(ClientName='Client A'),
  Client(ClientName='Client B'),
  Client(ClientName='Client C'),
]



def test_index(testapp):
    index = testapp.get('/')
    assert b'<p>Title: </p>' in index.data

def test_get_feature_requests(testapp):
    feature_requests = testapp.get('/feature-request')
    assert b'<th id="title">Title</th>' in feature_requests.data

def test_add_feature_request(testapp):
    session.bulk_save_objects(clients)
    session.commit()
    date1 = datetime.date.today() + datetime.timedelta(days=1)
    request_data = {
        "Title": "title", 
        "Description": "description",
        "ClientID": 1,
        "ProductArea": "Policy",
        "TargetDate": str(date1),
        "ClientPriority": 1
    }
    resp = testapp.post('/feature-request', content_type='application/json', data=json.dumps(request_data))

    assert 'Success' in json.loads(resp.data.decode('utf-8'))['message']
    assert FeatureRequest.query.filter_by(Title="title").count() == 1
    assert Client.query.filter_by(id=1).count() == 1

    resp_no_data = testapp.post('/feature-request', content_type='application/json', data=json.dumps({}))
    assert 'No input data provided' in json.loads(resp_no_data.data)['message']

    resp_with_errors = testapp.post('/feature-request', content_type='application/json', data=json.dumps({'Title':5}))
    assert 'error' in json.loads(resp_with_errors.data)['status']

    resp_with_clashing_priority1 = testapp.post('/feature-request', content_type='application/json', data=json.dumps(request_data))
    assert 'Success' in json.loads(resp_with_clashing_priority1.data)['message']
    assert FeatureRequest.query.filter_by(Title="title").count() == 2
    assert FeatureRequest.query.filter_by(ClientPriority=1, ClientID=1).count() == 1
    assert FeatureRequest.query.filter_by(ClientPriority=1, ClientID=1, id=2).count() == 1

    request_data["ClientPriority"] = 5
    resp_with_clashing_priority2 = testapp.post('/feature-request', content_type='application/json', data=json.dumps(request_data))
    assert 'Success' in json.loads(resp_with_clashing_priority2.data)['message']
    assert FeatureRequest.query.filter_by(Title="title").count() == 3
    assert FeatureRequest.query.filter_by(ClientPriority=5, ClientID=1).count() == 1
    assert FeatureRequest.query.filter_by(ClientPriority=1, ClientID=1).count() == 1
    assert FeatureRequest.query.filter_by(ClientPriority=1, ClientID=1).count() == 1

    request_data["ClientPriority"] = 1
    resp_with_clashing_priority2 = testapp.post('/feature-request', content_type='application/json', data=json.dumps(request_data))
    assert 'Success' in json.loads(resp_with_clashing_priority2.data)['message']
    assert FeatureRequest.query.filter_by(Title="title").count() == 4
    assert FeatureRequest.query.filter_by(ClientPriority=5, ClientID=1).count() == 1
    assert FeatureRequest.query.filter_by(ClientPriority=1, ClientID=1).count() == 1
    assert FeatureRequest.query.filter_by(ClientPriority=1, ClientID=1).count() == 1
    assert FeatureRequest.query.filter_by(ClientPriority=3, ClientID=1, id=1).count() == 1

def test_cleanUp(testapp):
    session.query(Client).delete()
    session.query(FeatureRequest).delete()
    session.execute("ALTER SEQUENCE clients_id_seq RESTART WITH 1")
    session.execute("ALTER SEQUENCE featurerequests_id_seq RESTART WITH 1")
    session.commit()
    assert Client.query.filter_by(id=1).count() == 0

