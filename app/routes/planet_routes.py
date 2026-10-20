from flask import Blueprint , abort , make_response, request, Response
from app.models.planets import Planet
from ..db import db
from app.routes.route_utilities import validate_model

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_new_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()
    return new_planet.to_dict(), 201

@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    name = request.args.get("name")

    if name:
        query = query.where(Planet.name == name)

    description = request.args.get("description")
    if description:
        query =  query.where(Planet.description.ilike(f"%{description}%")) 

    has_rings = request.args.get("has_rings")
    if has_rings:
        query = query.where(Planet.has_rings == has_rings)     

    
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
            
    return planets_response, 200

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet,planet_id)

    return planet.to_dict(),200

@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet,planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.has_rings = request_body["has_rings"]
    planet.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet,planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


