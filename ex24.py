print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem ="""
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere  there is none.
"""

print("------------------------")
print(poem)
print("------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	creates = jars / 100
	return jelly_beans, jars, creates

start_point = 10000
beans, jars, creates = secret_formula(start_point)

# REMEMBER THAT THIS IS ANOTHER WAY TO FORMAT A STRING 

print("Whit a starting point of: {}".format(start_point))

# it's just like with an f"" string

print(f"We'd have {beans} beans, {jars} jars, and {creates} creates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

# THIS IS AN EASY WAY TO APPLY A LIST TO A FORMAT STRING
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))	
