class Dog(object):
	def __init__(self, dog_name):
		self.dog_name = dog_name

	def __repr__(self) -> str:
		return(f"Dog(dog_name={self.dog_name})")

