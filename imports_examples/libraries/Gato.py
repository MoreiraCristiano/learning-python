
# Import de modulo que esta dentro da pasta src/model/
import sys
sys.path.append(".")
from src.model.Dog import Dog


class Gato(object):
	def __init__(self, name):
		self.name = name

	def __repr__(self) -> str:
		return(f"Gato(name={self.name})")

	def maior_inimigo(self):
		inimigo = Dog("DOGAO")
		return (f"inimigo ali: {inimigo.dog_name}")

