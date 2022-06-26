# Importacoes de classes que estao em pastas do mesmo nivel do arquivo main.py
from model.Person import Person
from model.Dog import Dog

# Importacoes de fora da pasta src (..); um nivel acima do arquivo main.py
import sys
sys.path.append("..")
from libraries.Gato import Gato


print(sys.modules)
print(sys.path)


p1 = Person("Cris", 10)
d1 = Dog("Rabento")
g1 = Gato("Gatomiau")

print(p1.__repr__())
print(d1.__repr__())
print(g1.__repr__())
print(g1.maior_inimigo())
