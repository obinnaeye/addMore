from flask_restful import Resource
from flask import Flask, render_template, make_response, jsonify, request
import json
from sqlalchemy import or_, and_
from Model import db, Client, ClientSchema, FeatureRequest, FeatureRequestSchema

clients_schema = ClientSchema(many=True)
client_schema = ClientSchema()
feture_requests_schema = FeatureRequestSchema(many=True)
feture_request_schema = FeatureRequestSchema()

class FeatureRequestResource(Resource):
  def get(self):
    print('We are here .....')
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template("index.html"))
  
  def post(self):
    json_data = json.loads(request.data)
    print(json_data)
    return json_data
    # if not json_data:
    #   return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    # data, errors = comment_schema.load(json_data)
    # if errors:
    #   return {"status": "error", "data": errors}, 422
    # return {"message": "New features"}