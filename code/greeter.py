def greet_user(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = greet_user('jenny', 'nicholson', age=12)
print(musician)

musician = greet_user('nikki', 'nicholson')
print(musician)