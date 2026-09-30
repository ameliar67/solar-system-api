from flask import Blueprint
from app.models.planets import planets

planet_bp = Blueprint("planet_bp",__name__)

@planet_bp.get("/")
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
        


