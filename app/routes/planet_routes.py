from flask import Blueprint , abort , make_response, request, Response
from app.models.planets import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_new_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    has_rings = request_body["has_rings"]

    new_planet = Planet(name=name, description=description, has_rings=has_rings)
    db.session.add(new_planet)
    db.session.commit()

    response = dict(
            id=new_planet.id, 
            name=new_planet.name, 
            description=new_planet.description,
            has_rings=new_planet.has_rings
        )

    return response, 201

@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "has_rings": planet.has_rings
            }
        )
    return planets_response, 200

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "has_rings": planet.has_rings
    }


@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.has_rings = request_body["has_rings"]
    planet.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)
    
    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet


            


    



        


