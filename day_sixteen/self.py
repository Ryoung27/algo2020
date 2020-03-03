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

class Comedian:
	def __init__(self, name, style, podcast):
		self.name = name
		self.style = style
		self.podcast = podcast
	def info(self):
		print(self.name + " is a " + self.style + " comedian " + self.podcast + " a podcast")

rogan = Comedian("Joe Rogan", "political", "with")
rogan.info()
