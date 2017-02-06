__author__ = 'anna'
import random

class Car(object):

    wheels = 4

    def __init__(self, make, model='Sonata'):
        self.make = make
        self.model = model
        print('The car is created')

    def __repr__(self):
        return self.make

    def drive(self):
        print('Car started...')

    def stop(self):
        print('Car stopped')

class RaceCar(Car):

    def __init__(self, make, model='Fast'):
        Car.__init__(self, make, model)
        print('The fast car is created')

    def accelerate(self):
        print('I will drive faster')

    def drive(self):
        super(RaceCar, self).drive()
        print('You are driving a Race Car')

    def stop(self):
        super(RaceCar, self).stop()
        print('Your car stopped very cool.')

car = Car('BMW')
print(car)
print(car.make, car.model)
car2 = Car('Benz', 5)
print(car2)
print(car2.make, car2.model)

print(Car.wheels)

race_car = RaceCar('Lamborgini')
print(race_car.model)
race_car.accelerate()
race_car.drive()
race_car.stop()
print(race_car)

class Fruit(object):

    def __init__(self, shape='Circle'):
        self.shape = shape
        print('New fruit is created... Its shape is {}'.format(self.shape))

    def nutrition(self, chemical):
        print('I am feading the fruit with {}'.format(chemical))

    def fruit_shape_change(self):
        shapes = ['Triangle', 'Oval','Square']
        shape = random.choice(shapes)
        self.shape = shape
        print('The shape of the fruit changed to {}'.format(shape))

class Watermelon(Fruit):

    def __init__(self, shape='Trapezoid', color=None):
        super(Watermelon, self).__init__(shape)
        self.color = color
        print('Also, this fruit has a color: {}'.format(self.color))

    def change_color(self):
        colors = ['Blue', 'Orange', 'Yellow']
        color = random.choice(colors)
        print('Changing color from {} to {}'.format(self.color, color))
        self.color = color

print('A Fruit instance:')
fruit = Fruit()
fruit.shape
fruit.fruit_shape_change()
print(fruit.shape)
fruit.nutrition('Yam!')

print('A Watermelon instance:')
watermelon = Watermelon(shape='Rectangle', color='Red')
watermelon.change_color()
print(watermelon.color)
watermelon.fruit_shape_change()
print(watermelon.shape)


