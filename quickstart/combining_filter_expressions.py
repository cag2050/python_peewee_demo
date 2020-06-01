from datetime import date

from quickstart.model_definition import Person

d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

for person in query:
    print(person.name, person.birthday)

query2 = (Person
         .select()
         .where(Person.birthday.between(d1940, d1960)))

for person in query2:
    print(person.name, person.birthday)
