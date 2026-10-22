from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")
    size: Mapped[str]
    description: Mapped[str]
    craters: Mapped[int]


    def to_dict(self):
        return dict(
            id=self.id,
            size=self.size,
            description=self.description,
            craters=self.craters
        )

    @classmethod
    def from_dict(cls,moon_data):
        new_data = cls(
            size=moon_data["size"],
            description=moon_data["description"],
            craters=moon_data["craters"]
        )
        return new_data
