__author__ = 'anna'
state_taxes = {'CA': 0.15, 'NY': 0.2, 'TX': 0.1}
fed_tax = 0.1

def net_income(state, gross_income):
    '''
    Calculate net income after federal and state taxes deduction.
    :param state:
    :param gross_income:
    :return:
    '''
    for item in state_taxes.items():
        if item[0] == state:
            state_tax = item[1]

            net_inc = gross_income - (gross_income * (fed_tax + state_tax))
            return net_inc
    else:
        return 'State is not in the list.'

print(net_income('CA', 100000))
print(net_income('NY', 100000))
print(net_income('YG', 100000))

def net_income_2(state, gross_income):
    '''
    Calculate net income after federal and state taxes deduction.
    :param state:
    :param gross_income:
    :return:
    '''
    if state in state_taxes:
        state_tax = state_taxes[state]
        net_inc = gross_income - (gross_income * (fed_tax + state_tax))
        return net_inc
    else:
        return 'State is not in the list.'

print('Second method:')
print(net_income_2('CA', 100000))
print(net_income_2('NY', 100000))
print(net_income_2('YG', 100000))

print(state_taxes.items())
