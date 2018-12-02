from flask import Blueprint
from flask_restful import Api
from resources.FeatureRequest import FeatureRequestResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(FeatureRequestResource, '/feature-request')
