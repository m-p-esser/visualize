"""Data models."""
from . import db

class Diagrams(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   synonyms = db.Column(db.String(100), nullable=True)
   goals = db.Column(db.String(100), nullable=False)
   visual_cues = db.Column(db.String(100), nullable=True)
   coordinate_system = db.Column(db.String(100), nullable=True)
   shapes = db.Column(db.String(100), nullable=True)
   related = db.Column(db.String(100), nullable=True)