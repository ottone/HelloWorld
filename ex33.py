# IN THIS EXERCISE YOU WILL LEARN THE WHILE-LOOP WHILE DOING THESE THREE CHECKS

i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)
	
	i = i + 1
	
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
	print(num)
