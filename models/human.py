import time
from datetime import datetime, date


class Human:
    planet: str = "Earth"
    populate: int = 0

    def __init__(
        self,
        name: str,
        date_of_birth: datetime
    ) -> None:
        self.__date_of_birth = date_of_birth
        self.name = name
        Human.populate += 1

    def get_age(self):
        return (datetime.now() - self.__date_of_birth)
    
    
Human.planet = "Vene"

print( Human.populate )

c1 = Human(
    name="Dmytro",
    date_of_birth=datetime(1996, 9, 24)
)
c2 = Human(
    name="Maxim",
    date_of_birth=datetime(2005, 1, 24)
)
print( Human.populate )

while 1:
    print(c1.name, c1.get_age())
    print(c2.name, c2.get_age())
    time.sleep(1)
