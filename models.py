from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()  


class Hero(db.Model):
    __tablename__ = 'hero'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String, nullable=False)
    
    
    hero_powers = db.relationship("HeroPower", backref="hero", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }
    
    
class Power(db.Model):
    __tablename__ = 'power'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    
    hero_powers = db.relationship("HeroPower", backref="power")
    
    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be present and at least 20 characters long.")
        return value
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
            
            
class HeroPower(db.Model):  
    __tablename__ = 'hero_power'
    
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)  
    power_id = db.Column(db.Integer, db.ForeignKey("power.id"), nullable=False)
    strength = db.Column(db.String, nullable=False)
    
    @validates("strength")
    def validate_strength(self, key, value):
        if value not in ["Strong", "Weak", "Average"]:
            raise ValueError("Strength must be either 'Strong', 'Weak', or 'Average'.")
        return value
    
    def to_dict(self):
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "strength": self.strength
        }
