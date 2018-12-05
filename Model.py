from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from sqlalchemy import UniqueConstraint
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    ClientName = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, ClientName):
        self.ClientName = ClientName


class FeatureRequest(db.Model):
    __tablename__ = 'featurerequests'
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(250), nullable=False)
    Description = db.Column(db.String(250), nullable=False)
    TargetDate = db.Column(db.DateTime, nullable=False)
    ClientPriority = db.Column(db.Integer, nullable=False)
    ProductArea = db.Column(db.String(250), nullable=False)
    ClientID = db.Column(db.Integer, db.ForeignKey('clients.id', ondelete='CASCADE'), nullable=False)
    client = db.relationship('Client', backref=db.backref('featurerequests', lazy='dynamic' ))

    def __init__(self, Title, Description, TargetDate, ClientPriority, ProductArea, ClientID):
        self.Title = Title
        self.Description = Description
        self.TargetDate = TargetDate
        self.ClientPriority = ClientPriority
        self.ProductArea = ProductArea
        self.ClientID = ClientID


class ClientSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    ClientName = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()

class FeatureRequestSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    Title = fields.String(required=True, validate=validate.Length(1))
    Description = fields.String(required=True, validate=validate.Length(1))
    TargetDate = fields.String(required=True, validate=validate.Length(1))
    ClientPriority = fields.Integer(required=True)
    ProductArea = fields.String(required=True, validate=validate.Length(1))
    ClientID = fields.Integer(required=True)
    creation_date = fields.DateTime()