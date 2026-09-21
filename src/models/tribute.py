class Tribute:
    def __init__(self, name, id, gender, age, district, speed, strength, personality):
        self.name = name
        self.id = id
        self.gender = gender
        self.age = age
        self.district = district
        self.speed = speed
        self.strength = strength
        self.personality = personality
        self.alive = True
        self.weapon = None
        self.position = None

    def __str__(self):
         return (
        f"Tribute Name: {self.name}, "
        f"Status: {self.status}, "
        f"Age: {self.age}, "
        f"ID: {self.id}, "
        f"District: {self.district}, "
        f"Speed: {self.speed}, "
        f"Strength: {self.strength}, "
        f"Personality: {self.personality}, "
        f"Weapon: {self.weapon}, "
        f"Position: {self.position}"
    )

