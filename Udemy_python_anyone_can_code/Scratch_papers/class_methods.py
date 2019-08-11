# creating a tiger class with attributes and methods

class Tiger(object):

    legs = 4

    def __init__(self, color='orange_black', age=3, name='Tiger'):
        self.color = color
        self.age = age
        self.name = name
        print('You created Tiger ' + self.name)
    def info_color(self):
        return 'Color:', self.color


    def roar(self, roar_times=1):
        return self.name + ' Roar!'* roar_times

    def aged(self, years=1):
        new_age = self.age + years
        self.age = new_age
        return new_age

class BengalTiger(Tiger):
    legs = 5

    def __init__(self, color='white', age=6, name='Default'):
        Tiger.__init__(self, color, age, name)
        self.color = color
        self.age = age
        self.name = name
        print('You created a Bengal tiger ' + self.name)

    #overwrite method of parent class:
    def roar(self, roar_times=2):

        return (super(BengalTiger, self).roar(roar_times), self.name + ' Roar!!!!!'* roar_times)


tiger_anya = Tiger(color='Red', age=5, name='Anya')
print(tiger_anya.roar(roar_times=3))

bengal = BengalTiger(color='white', age=10, name='Umka')
print(bengal.roar())
bengal2 = BengalTiger()
print(bengal2.roar())
print(BengalTiger.legs)
print ('----------back to school 7/21/19-----------')

# back to school 7/21/19

class Motorcycle(object):

    wheels = 4
    headlights = 2

    def __init__(self, make, color):
        print('Created general mc')
        self.make = make
        self.color = color

    def info(self):
        print('Make: {}'.format(self.make))
        print('Color: {}'.format(self.color))

    def drive(self):
        print('Started')

    def stop(self):
        print('Stopped')

class SportMotorcycle(Motorcycle):

    def __init__(self, make, color):
        print('Created SportMc')
        Motorcycle.__init__(self, make, color)

    def drive(self):
        super(SportMotorcycle, self).drive()
        print('Started SportMC')

mc1 = Motorcycle('Honda', 'Red')
print(mc1.wheels)
print(mc1.make, mc1.color)
mc1.info()

mc2 = SportMotorcycle('Acura', 'Blue')
mc2.info()
mc2.drive()