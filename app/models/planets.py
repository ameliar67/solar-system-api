from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from sqlalchemy import ForeignKey
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    has_rings: Mapped[bool]
    moons: Mapped[Optional[list["Moon"]]] = relationship(back_populates="planet")


    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["has_rings"]=self.has_rings
        if self.moons:
            planet_as_dict["moons"]=[moon.to_dict() for moon in self.moons]
        return planet_as_dict

    @classmethod
    def from_dict(cls,planet_data):
        new_data = cls(
            name=planet_data["name"],
            description=planet_data["description"],
            has_rings =planet_data["has_rings"]

        )
        return new_data

