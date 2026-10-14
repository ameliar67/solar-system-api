from flask import Blueprint , abort , make_response, request
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


            


    



        


