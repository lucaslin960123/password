password = 'a123456'
b = 3
while True:
	a = input('Enter the password:')
	if a == password:
		print('You are right!')
		break
	else:
		b = b-1	
		print('Try it again,you got',b,'more chance')
		if b == 0:
			print('You dont have any chances left, try it next time')
			break