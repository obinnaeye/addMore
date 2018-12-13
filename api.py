from flask import Blueprint
from flask_restful import Api
from resources.FeatureRequest import FeatureRequestResource
from resources.Home import HomeResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(FeatureRequestResource, '/feature-request')
api.add_resource(HomeResource, '/')
