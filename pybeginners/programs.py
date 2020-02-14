# Find odd/even
def oddeven(number):
	try:
		if int(number) % 2:
			return 'odd'
		else:
			return 'even'
	except:
		raise Exception("Argument must be valid integer")

# Check prime
def isprime(number):
	try:
		n = int(number)
		if n < 2:
			raise Exception("Prime numbers start from 2")
		for i in range(2,n):
			if not n%i:
				return 'not prime'
		else:
			return 'prime'
	except:
		raise Exception("Argument must be valid integer")

# Check perfect square
def issquare(number):
	try:
		n = int(number)
	except:
		raise Exception("Argument must be valid integer")
	if n < 1:
		raise Exception("Number must be a positive integer")
	flag = False
	for i in range(n+1):
		if i*i > n:
			return 'not square'
		if i*i == n:
			return 'square'

# Check perfect cube
def iscube(number):
	try:
		n = int(number)
	except:
		raise Exception("Argument must be valid integer")
	if n < 1:
		raise Exception("Number must be a positive integer")
	flag = False
	for i in range(n+1):
		if i*i*i > n:
			return 'not cube'
		if i*i*i == n:
			return 'cube'

