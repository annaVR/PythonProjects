__author__ = 'anna'

import sys

def except_handling(a, b):
    try:
        print(a / b)
    # except ZeroDivisionError as zd:
    #     print('ZeroDivisonError: {}'.format(zd))
    # except TypeError as ty:
    #     print('TypeError: {}'.format(ty))
    except:
        print('Unexpected error: {}, {}, {}'.format(sys.exc_info()[0],
                                                    sys.exc_info()[1], sys.exc_info()[2]))
        #raise
except_handling(5, 0)
except_handling(5, 'Anna')

car = {'make': 'BMW', 'model': '6', 'year': 2015}

def exc_hand_dict(key):
    try:
        print(car[key])
    except KeyError as err:
        print('The error is KeyError: {}'.format(err))
    finally:
        print('All done.')

exc_hand_dict('make')
exc_hand_dict('color')

