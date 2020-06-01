from quickstart.model_definition import Person, Pet

for pet in Pet.select().join(Person).where(Person.name == 'Herb').order_by(Pet.name):
    print(pet.name)

for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name + ': ' + str(person.birthday))
