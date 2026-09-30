from flask import Blueprint , abort , make_response
from app.models.planets import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    planets_return = []
    for planet in planets:
        planets_return.append(
            dict(
                id= planet.id,
                name = planet.name,
                description  = planet.description,
                has_rings = planet.has_rings
            )
        )
    return planets_return


            
@planet_bp.get("/<id>")
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

    



        


