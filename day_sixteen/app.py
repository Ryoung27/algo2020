class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		print(self.first + ' ' + self.last)

emp_1 = Employee("Richie", "Y", 0.00)
emp_2 = Employee("Test", "U", 10.00)

#print(emp_1)
#print(emp_2)

print(emp_1.first)
print(emp_2.first)
emp_1.fullname()
emp_2.fullname()
