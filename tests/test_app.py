import datetime
import json
from Model import Client, FeatureRequest

def test_index(testapp):
    index = testapp.get('/')
    assert b'<p>Title: </p>' in index.data

def test_get_feature_requests(testapp):
    feature_requests = testapp.get('/feature-request')
    assert b'<th id="title">Title</th>' in feature_requests.data

def test_add_feature_request(testapp):
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

    assert FeatureRequest.query.filter_by(Title="title").count() == 1
    assert Client.query.filter_by(id=1).count() == 1


# import pytest
# import app as _app
# from Model import db as _db, FeatureRequest, Client




# @pytest.fixture('module')
# def client():
#     app = _app.create_app('test_config')
#     client = app.test_client()
#     return client

# # @pytest.fixture('module')
# # def teardown():
# #     db.session.remove()
# #     db.drop_all()
# #     db.get_engine(app).dispose()

# def test_index(client):
#     index = client.get('/')
#     assert b'<p>Title: </p>' in index.data

# def test_get_feature_requests(client):
#     feature_requests = client.get('/feature-request')
#     assert b'<th id="title">Title</th>' in feature_requests.data

#     post_feature_requests = client.post('/feature-request')
#     assert b'nothing' in post_feature_requests.data

