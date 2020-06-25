class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am", self.name + "!")


person = Person(input().strip())
person.greet()