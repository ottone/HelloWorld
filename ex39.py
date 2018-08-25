# CREATE A MAPPING OF STATE TO ABBREVIATION

states = { 
	'Oregon'    : 'OR',
	'Florida'   : 'FL',
	'California': 'CA',
	'New York'  : 'NY',
	'Michigan'  : 'MI'
}

# CREATE A BASIC SET OF STATES AND SOME CITIES IN THEM

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Ditroit',
	'FL' : 'Jacksonville'
}

# ADD SOME MORE CITIES

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# PRINT OUT SOME CITIES

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# PRINT SOME STATES

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida has: ", states['Florida'])

# DO IT BY USING THE STATE THEN CITIES DICT

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# PRINT EVERY STATE ABBREVIATION

print('-' * 10)
for state, abbrev in list(states.items()): # LA FUNZIONE LIST CONVERTE IN LISTA MENTRE ITEMS FORNISCE DELLE COPPIE DI VALORI SULLE QUALI ITERATE
	print(f"{state} is abbreviated {abbrev}")

# PRINT EVERY CITY IN STATE

print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# NOW DO BOTH AT THE SAME TIME

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 10)

# SAFELY GET A ABBREVIATION BY STATE THAT MIGHT NOT BE THERE

state = states.get('Texas') # DIZIONARIO.GET('CHIAVE') RESTITUISCE IL VALORE SE PRESENTE ALTRIMENTI NONE
if not state:
	print("Sorry, no Texas.")
	
# GET A CITY WITH A DEFAULT VALUE
city = cities.get('TX', 'Does Not Exist')  # DIZIONARIO.GET('CHIAVE', 'DEFAULT' ) RESTITUISCE IL VALORE SE PRESENTE ALTRIMENTI IL DEFAULT 
print(f"The city for the state 'TX' is : {city}")
