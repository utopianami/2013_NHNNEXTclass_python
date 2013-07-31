class person:
	def __init__(self, moeny):
		self.person_moeny = moeny
		self.bought = []

	def input_moeny(self, machine, moeny):	
		self.person_moeny -= moeny	
		machine.machine_moeny += moeny

	def select_product(self, machine, choice):
		self.bought = machine.select_product(choice)
		

	def get_change(self, machine):
		self.person_moeny += machine.return_change()



class machine:
	def __init__(self):
		self.init_product()
		self.machine_moeny = 0

	def init_product(self):
		
		self.product = {}


	def sell_product(self, choice):
		if (self.machine_moeny) < self.product[choice][price]:
			return '잔액부족'
		if self.product[choice][count] == 0:
			return "매진"

		self.product[choice][count]-
		self.machine_moeny - self.product[choice][price]

		return
			product[choice]



	def return_change(self):
		temp = machine_moeny
		machine_moeny = 0
		return temp




'''
flow
0. init


1. def input_moeny()
	
	return
		class person : person_moeny -
		class machine : machine_moeny +

2. def select_product()
	
	return
		class machine : def sell_product()

3. def sell_product()
	
	check : 잔액비교 + 매진여부

	
	self.product[choice][count]-
	self.machine_moeny - self.product[choice][price]

	return
		person.bought = product[choice]

4. def get_change()
	machine.return_change()


5. return_change()
	return
		moeny
