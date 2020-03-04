class Monster:
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def info(self):
		print(self.name + " can do " + self.power)

test = Monster("test", "unit")

test.info()
