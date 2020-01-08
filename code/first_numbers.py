values = range(1, 1_000_001)
print("Minimum: " + str(min(values)))
print("Maximum: " + str(max(values)))
print("Sum: " + str(sum(values)))

odds = range(1, 21, 2)
for odd in odds:
    print(odd)

threes = range(3, 31, 3)
for three in threes:
    print(three)

cubes = []
values = range(1, 11)
for value in values:
    cubes.append(value ** 3)

cubes = [value ** 3 for value in range(1, 11)]

for cube in cubes:
    print(cube)
