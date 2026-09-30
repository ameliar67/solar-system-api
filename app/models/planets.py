class Planet:
    def __init__(self,id,name,description,has_rings):
        self.id = id
        self.name = name  
        self.description = description
        self.has_rings = has_rings

planets = [
    Planet(1 , "Mercury" , "It is the smallest planet in the solar system and it is nearest to sun " , False),
    Planet(2 , "Jupiter" , " its a largest planet in the solar system , it has lot of moons" , True),
    Planet(3 , "Earth" , "The only place in our solar system have living things" ,False)
]