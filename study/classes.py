class Dog():

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name + "is sitting")


test_dog = Dog('ben', 54)

test_dog.sit()

class WildDog(Dog):

    def __init__(self, name, age, sd) -> None:

        super().__init__(name, age)
        
        self.sd = sd

new_test = WildDog('a', '231', 'newone')
print(new_test.sd)