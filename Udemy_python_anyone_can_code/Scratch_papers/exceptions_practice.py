def exception_handling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b)/c
        print(d)
    except:
        print('Exception happend')
        #raise Exception('This is raised')
    else:
        print('Else executed')
    finally:
        print('Finally, always executed')

cars = dict(make = 'hyundai', model = 'sonata', year = 2015)
def except_cars():
    try:
        print(cars['color'])
    except:
        # raise Exception('Here is the dictionary exception:')
        print('Exception handled')
    else:
        print('This is else block')
    finally:
        print('Execution finished: this is the finally block')

exception_handling()
except_cars()