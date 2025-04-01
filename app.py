from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower
from flask_migrate import Migrate

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Routes
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the SuperHeroes API!"})

# GET route for all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()  
    heroes_list = [hero.to_dict() for hero in heroes]
    return jsonify(heroes_list)

# GET route for a specific hero
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    hero_data = hero.to_dict()
    hero_data["hero_powers"] = [hp.to_dict() for hp in hero.hero_powers]
    return jsonify(hero_data)

# GET route for all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_list = [power.to_dict() for power in powers] 
    return jsonify(powers_list)

# GET route for a specific power
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

# PATCH route to update a power's description
@app.route('/powers/<int:id>', methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()
    description = data.get("description")
    if not description:
        return jsonify({"error": "Description is required"}), 400
    
    try:
        power.description = description  
        db.session.commit()
        return jsonify(power.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# POST route to create a new HeroPower
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    strength = data.get("strength")
    
    #validation
    if not hero_id or not power_id or not strength:
        return jsonify({"errors": ["hero_id, power_id, and strength are required."]}), 400
        
    try:
        new_hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
        db.session.add(new_hero_power)
        db.session.commit()
        
        response = new_hero_power.to_dict()
        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)
        response["hero"] = hero.to_dict() if hero else None
        response["power"] = power.to_dict() if power else None
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
