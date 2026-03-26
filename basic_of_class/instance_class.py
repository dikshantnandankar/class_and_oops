
class Animal:

    name_of_animal = 'start'
    animal_sound = 'start'

    def __init__(self,nameOfanimal,AnimalSound):

        self.name_of_animal = nameOfanimal
        self.animal_sound = AnimalSound

        print('inside class animal name', self.name_of_animal)
        print('inside class animal sound' , self.animal_sound)


# invoke
an1 = Animal('dog','bark')

print('outside of class animal sound', an1.animal_sound)
print('outside of class name of animal ', an1.name_of_animal)

an2 = Animal('cat', 'meow')
