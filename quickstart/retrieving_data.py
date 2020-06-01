from quickstart.model_definition import Person, Pet

grandma = Person.select().where(Person.name == 'Grandma L.').get()
print(grandma.name)

for person in Person.select():
    print(person.name)

query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name + ', owner: ' + pet.owner.name)

query2 = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))
for pet in query2:
    print(pet.name + ', owner:: ' + pet.owner.name)

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)


