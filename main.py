from models import Human, Student

person = Human(
    name="Dmytro",
    father_name="Igorovich",
    age=27,
    posXY=(0, 0),
)
stud = Student(
    name="Dmytro",
    father_name="Igorovich",
    age=27,
    posXY=(0, 0),
    school="KNTU",
)

stud.spell_words('math', '1 + 1 = 2')
person.spell_words('math is good')