from flask import Blueprint , abort , make_response, request, Response
from app.models.planets import Planet
from app.models.moon import Moon
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


@planet_bp.post("<planet_id>/moons")
def create_new_moon(planet_id):

    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    try:
        new_moon = Moon.from_dict(request_body)
    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))
    new_moon.planet_id = planet.id

    db.session.add(new_moon)
    db.session.commit()
    return new_moon.to_dict(), 201


@planet_bp.get("<planet_id>/moons")
def get_moons(planet_id):
    planet = validate_model(Planet,planet_id)

    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_dict())
            
    return moons_response, 200
