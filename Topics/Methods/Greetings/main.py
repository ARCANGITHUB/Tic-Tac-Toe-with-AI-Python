class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}!"


greeting = Person(input()).greet()

print(greeting)
