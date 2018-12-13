from flask_restful import Resource
from flask import Flask, render_template, make_response, jsonify, request
import json
from sqlalchemy import or_, and_
from Model import db, Client, ClientSchema, FeatureRequest, FeatureRequestSchema
from resources.misc.script import sql

clients_schema = ClientSchema(many=True)
client_schema = ClientSchema()
feture_requests_schema = FeatureRequestSchema(many=True)
feture_request_schema = FeatureRequestSchema()

class FeatureRequestResource(Resource):
  def get(self):
    client_mapping = {
      1: 'Client A',
      2: 'Client B',
      3: 'Client C'
    }
    headers = {'Content-Type': 'text/html'}
    features = FeatureRequest.query.all()
    featurerequests = feture_requests_schema.dump(features).data
    return make_response(render_template("requests.html", featurerequests=featurerequests, client_mapping=client_mapping))
  
  def post(self):
    json_data = json.loads(request.data)
    if not json_data:
      return {'message': 'No input data provided'}, 400
    data, errors = feture_request_schema.load(json_data)
    if errors:
      return {"status": "error", "data": errors}, 422
    priority_clash = FeatureRequest.query.filter(
                      and_(FeatureRequest.ClientPriority==data['ClientPriority'], 
                      FeatureRequest.ClientID==data['ClientID'])
                    ).first()
    if priority_clash :
      db.engine.execute(sql, newClientPriority=int(data['ClientPriority']), newClientID=int(data['ClientID'])) 
                
    feature_request = FeatureRequest( 
      Title=data['Title'], 
      Description=data['Description'],
      TargetDate=data['TargetDate'],
      ClientPriority=data['ClientPriority'],
      ProductArea=data['ProductArea'],
      ClientID=data['ClientID']
    )
    db.session.add(feature_request) 
    db.session.commit() 
    return { 'message': 'Success' } 