class Cat:
    def speak(self):
        print("meow")

class Dog:
    def speak(self):
        print("woof")

def speak(pet):
    pet.speak()

cat = Cat()
speak(cat)
dog = Dog()
speak(dog)