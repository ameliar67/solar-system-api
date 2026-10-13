from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    has_rings: Mapped[bool]

planets = [
    # Planet(1 , "Mercury" , "It is the smallest planet in the solar system and it is nearest to sun " , has_rings=False),
    # Planet(2 , "Jupiter" , " its a largest planet in the solar system , it has lot of moons" , has_rings=True),
    # Planet(3 , "Earth" , "The only place in our solar system have living things" ,has_rings=False)
]
