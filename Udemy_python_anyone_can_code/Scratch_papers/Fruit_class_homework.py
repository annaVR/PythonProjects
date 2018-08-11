class Fruit(object):

    def __init__(self, shape='round', size='small'):
        self.shape = shape
        self.size = size
        print('I am {} {} generic fruit'.format(self.size, self.shape))

    def nutrition(self):
        return 'Give me {} amount of nutrition'.format(self.size)

    def fruit_shape(self):
        return 'I have a {} shape'.format(self.shape)

class Lemon(Fruit):

    def __init__(self, shape='oval', size='big'):
        Fruit.__init__(self, shape, size)
        self.shape = shape
        self.size = size
        print('Actualy, I am not generic any more. I am a lemon.')

    def 

fruit = Fruit()

print(fruit.fruit_shape())
print(fruit.nutrition())

lemon = Lemon()