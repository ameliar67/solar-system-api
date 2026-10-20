from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    has_rings: Mapped[bool]


    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            has_rings=self.has_rings
        )

    @classmethod
    def from_dict(cls,planet_data):
        new_data = cls(
            name=planet_data["name"],
            description=planet_data["description"],
            has_rings =planet_data["has_rings"]

        )
        return new_data

