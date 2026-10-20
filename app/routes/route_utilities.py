from flask import abort, make_response
from ..db import db


def validate_model(cls,id):
    try:
        planet_id = int(id)
    except:
        response = {"message": f"{cls.__name__} {planet_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(cls).where(cls.id == planet_id)
    planet = db.session.scalar(query)
    
    if not planet:
        response = {"message": f"{cls.__name__} {planet_id} not found"}
        abort(make_response(response, 404))

    return planet