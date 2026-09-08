class animal:
    def eat(self):
        print("Animal sound")

class dog:
    def bark(self):
        print("bark")

class cats:
    def sound(self):
        print("Meow")
animals = [dog(), cats()]
for animal in animals:
    animal.sound()