class Artist:
	def __init__(self, name, field, living):
		self.name = name
		self.field = field
		self.living = living

	def rundown(self):
		print(self.name + " is a " + self.field + " and is " + self.living)

yae = Artist("Kanye", "artist", "alive")
yae.rundown()

picaso = Artist("Pablo", "painter", "dead")
picaso.rundown()

jobs = Artist("Steve", "designer", "dead")
jobs.rundown()
