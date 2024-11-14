persons = {"John": 123, "Jo": 456, "Fo": 789}
print(persons.keys())
print(persons.values())

for person in persons.keys():
    print(person)

for person_value in persons.values():
    print(person_value)

for pers in persons:
    print(f"{pers}:{persons[pers]}")

for pers in persons.items():
    name, height = pers
    print(name, height)

for name, height in persons.items():
    print(f"{name}: {height}")