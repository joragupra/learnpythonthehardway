i = 0
numbers = []

while i < 6:
	print "At the topi is %d" % i
	numbers.append(i)

	i = i + 1
	print "umbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num

def create_numbers_with_increment(num_elements, increment):
	numbers = []
	i = 0
	while i < num_elements:
		numbers.append(i)
		i = i + increment
	return numbers

def create_numbers(num_elements):
	return create_numbers_with_increment(num_elements, 1)

def create_numbers_with_range(num_elements, increment):
	return range(0, num_elements - 1, increment)

print "Now using 'create_numbers' function."
nelements = 8
print "Numbers with %d elements:" % nelements
numbers = create_numbers(nelements)
for num in numbers:
	print num

print "Now using 'create_numbers' function."
nelements = 10
print "Numbers with max. value %d." % nelements
numbers = create_numbers(nelements)
for num in numbers:
	print num

print "Now using 'create_numbers_with_increment' function."
nelements = 8
increment = 2
print "Numbers with max. value %d." % nelements
print "Increment is %d increment." % increment
numbers = create_numbers_with_increment(nelements, increment)
for num in numbers:
	print num

print "Now using 'create_numbers_with_range' function."
nelements = 8
increment = 2
print "Numbers with max. value %d." % nelements
print "Increment is %d increment." % increment
numbers = create_numbers_with_range(nelements, increment)
for num in numbers:
	print num