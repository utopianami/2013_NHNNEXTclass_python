class father() :
	c=5
	def __init__(self, name):
		self.b = 3
		self.age = 23

		
	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
		print self.age
		print c 
		#print self.age
		


			
a = father('2323')


a.setName('test')
