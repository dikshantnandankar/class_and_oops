
class Animal:

    name_of_animal = 'start'
    sound = 'start'

    def __init__(self,nameOfanimal):
        name_of_animal = 'test'
        print('this is class init method')
        print('self' , self)
        print('animal name' , self.name_of_animal)
        print('animal sound' , self.sound)
        print('name of animal local ' , name_of_animal)
        self.name_of_animal = nameOfanimal
        self.sound = 'bark'
        name_of_animal = 'test2'
        print('animal name', self.name_of_animal)
        print('animal sound' , self.sound)
        print('name of animal local ' , name_of_animal)

# invoke
an1 = Animal('dog')
print('-'*10)
an2 = Animal('cat')