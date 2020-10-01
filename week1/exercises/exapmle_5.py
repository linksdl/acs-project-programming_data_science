

list_of_names = ['Fred','George','Sam']

for name in list_of_names:
    print('Hello {}, nice to meet you!'.format(name))


people_and_places = {
    'John': {'home': 'Leeds', 'born': 'Paris', 'parents': 'Paris'},
    'Fred': {'home': 'Barcelona', 'born': 'Madrid', 'parents': 'Oviedo'},
    'George': {'home': 'London', 'born': 'Bristol', 'parents': 'Exeter'},
    'Sam': {'home': 'Munich', 'born': 'Berlin', 'parents': 'Munich'}
}

for name, data in people_and_places.items():
    print('{} lives in {}. He was born in {} and his parents live in {}.'.format(name, data['home'], data['born'], data['parents']))
