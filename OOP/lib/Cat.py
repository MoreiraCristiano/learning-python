import sys
sys.path.append(".")
from .Pet import Pet


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("MEOOOOOOOOOOOOOOW")

    def show(self):
        print(
            f"I am {self.name} and i am {self.age} years old and my color is {self.color}"
        )

