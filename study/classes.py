class Dog():

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name + "is sitting")


test_dog = Dog('ben', 54)

test_dog.sit()