def Descending_Order(num):
	print((sorted(str(num), reverse=True)))
	return int("".join(sorted(str(num), reverse=True)))
	

print (Descending_Order(11223344551277899))