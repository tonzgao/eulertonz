divisors = [x for x in range(11, 21)]

def sm():
	num = 20*19
	while test(num) != True:
		num = num + 20
	return num

def test(num):
  for x in divisors:
    if (num % x) != 0:
      return False
  return True

print sm()