class player():
	def __init__(self):
		self.x = 0
		self.y=0
		self.image="./art/playerImage.png"
		self.name="blonic"
		self.health="10"
		self.speed="2"
		self.activeItem=None
		self.items=[]

	def equipItem(self, item):
		self.items.append(item)

	def move(self, xDir, yDir):
		self.x += self.speed * xDir
		self.y += self.speed * yDir

	def useActiveItem(self):
		self.activeItem.use()

	def draw(self):
		window.blit(self.image, (self.x, self.y))

