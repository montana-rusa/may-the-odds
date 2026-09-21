import json
import math
import random

from faker import Faker

from ..models.tribute import Tribute

tributes_file = "data/tributes.json"

NAME_METHOD = {
    "female": "first_name_female",
    "male": "first_name_male",
}

#tributes = [name, id, gender, age, district, speed, strength, personality]

def create_tributes():
    tributes = []
    for id in range(1, 25):
        gender = "female" if id % 2 == 0 else "male"
        new_tribute = Tribute(
            gender=gender,
            name=getattr(Faker(), NAME_METHOD[gender])(),
            id=id,
            age=random.randint(12, 18),
            district=math.ceil(id / 2),

            #TODO change this to point-based system instead of random
            speed=random.randint(1, 10),
            strength=random.randint(1, 10),
            personality=random.randint(1, 10)
        )
        tributes.append(new_tribute)

    return tributes

def write_tributes_to_json(tributes):
    with open(tributes_file, "w") as f:
        json.dump([tribute.__dict__ for tribute in tributes], f, indent=2)

create_tributes()
write_tributes_to_json(create_tributes())

