class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say_hi(self) -> str:
		return "Hello every1"

	def __repr__(self) -> str:
		return (f"Person(name={self.name}, age={self.age})")

