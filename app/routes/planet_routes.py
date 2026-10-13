from flask import Blueprint , abort , make_response, request
from app.models.planets import planets
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    query = db.select(planets).order_by(planets.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description
            }
        )
    return planets_response


            
@planet_bp.post("")
def get_one_planet(id):
    try:
        id = int(id)
    except ValueError:
        response = {"message" : f"planet {id} invalid"}
        abort(make_response(response,400))
    for planet in planets:
        if planet.id == id :
            return dict(
                        id= planet.id,
                        name = planet.name,
                        description  = planet.description,
                        has_rings = planet.has_rings
                    )
    
    response = {"message" : f"planet {id} not found"}
    abort(make_response(response,404))

    



        


