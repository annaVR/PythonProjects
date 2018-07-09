# creating a tiger class with attributes and methods

class Tiger(object):

    def __init__(self, color='orange_black', age=3, name='Tiger'):
        self.color = color
        self.age = age
        self.name = name

    def roar(self, roar_times=1):
        return self.name + ' Roar!'* roar_times

    def aged(self, years=1):
        new_age = self.age + years
        self.age = new_age
        return new_age

tiger_anya = Tiger(color='Red', age=5, name='Anya')
print(tiger_anya.roar(roar_times=3))
print(tiger_anya.age)
print(tiger_anya.aged(2))
print(tiger_anya.age)
