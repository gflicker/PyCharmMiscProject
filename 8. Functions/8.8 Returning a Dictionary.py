#Making a name of a person using values as parameters
def someones_name(first_name, last_name):
    """Returning a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

name = someones_name('Caramel', 'Princessa')
print(name)

print("\nThis is how it look when we add more parameters")

def build_person(first_name, last_name, age=None):
    """Returns a dictionary with information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

name = build_person('Caramel', 'Princessa', age = 20)
print(name)