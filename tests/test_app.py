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
    print(json.loads(resp.data))
    assert 'Success' in json.loads(resp.data)['message']
    assert FeatureRequest.query.filter_by(Title="title").count() == 1
    assert Client.query.filter_by(id=1).count() == 1

    resp_no_data = testapp.post('/feature-request', content_type='application/json', data=json.dumps({}))
    assert 'No input data provided' in json.loads(resp_no_data.data)['message']

    resp_with_errors = testapp.post('/feature-request', content_type='application/json', data=json.dumps({'Title':5}))
    assert 'error' in json.loads(resp_with_errors.data)['status']

    resp_with_clashing_priority = testapp.post('/feature-request', content_type='application/json', data=json.dumps(request_data))
    assert 'Success' in json.loads(resp_with_clashing_priority.data)['message']
    assert FeatureRequest.query.filter_by(Title="title").count() == 2
