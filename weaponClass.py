class weapon():
	def __init__(self):
		self.x = 0
		self.y=0
		self.image="./art/meow.png"
	def draw(self):
		window.blit(self.image, (self.x, self.y))

