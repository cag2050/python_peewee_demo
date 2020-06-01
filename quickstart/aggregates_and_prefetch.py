from peewee import JOIN, fn

from quickstart.model_definition import Person, Pet

for person in Person.select():
    print(person.name + ': ' + str(person.pets.count()), 'pets')

# Peewee provides a magical helper fn(), which can be used to call any SQL function. In the above example, fn.COUNT(Pet.id).alias('pet_count') would be translated into COUNT(pet.id) AS pet_count.
query = (Person
         .select(Person, fn.COUNT(Pet.id).alias('pet_count'))
         .join(Pet, JOIN.LEFT_OUTER)
         .group_by(Person)
         .order_by(Person.name))

for person in query:
    # "pet_count" becomes an attribute on the returned model instances.
    print(person.name, person.pet_count, 'pets')