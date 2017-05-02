import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/woocommerce_api_testing')

import json
from tools import request
from tools import helpers


rq = request.Request()
helper = helpers.Helper()

def test_create_customer():
    '''

    :return:
    '''
    global email
    global username
    global first_name
    global last_name
    global customer_id
    global input_data

    print('TC1, customers endpoint, pos, create customer.')
    generated_info = helper.generate_customer_info()
    email = generated_info['email']
    username = generated_info['username']
    first_name = generated_info['first_name']
    last_name = generated_info['last_name']

    input_data = {
        'customer': {

        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "billing_address": {
            "first_name": first_name,
            "last_name": last_name,
            "company": "",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US",
            "email": email,
            "phone": "(555) 555-5555"
        },
        "shipping_address": {
            "first_name": first_name,
            "last_name": last_name,
            "company": "",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US"
        }
    }
    }

    rs = rq.post('customers', input_data)

    # verify the response code before parsing the response body

    assert rs[0] == 201, '"Customers" endpoint failed. Status code expected: {}. Returned: {}'.format(201, rs[0])

    print(rs)
    # for item in rs:
    #     if isinstance(item, dict):
    #         print(json.dumps(item, indent=4))
    #     print(item)

    # if assert is successful, parse response body

    rs_body = rs[1]['customer']
    customer_id = rs_body['id']
    print('Customer id: {}'.format(customer_id))
    assert rs_body['email'] == email, '"email" in response is not as expected. Expected: {}. Returned: {}.'.format(email, rs_body['email'])
    assert rs_body['username'] == username, '"username" in response is not as expected. Expected: {}. Returned: {}.'.format(username, rs_body['username'])
    assert rs_body['first_name'] == first_name, '"first_name" in response is not as expected. Expected: {}. Returned: {}.'.format(first_name, rs_body['first_name'])
    assert rs_body['last_name'] == last_name, '"last_name" in response is not as expected. Expected: {}. Returned: {}.'.format(last_name, rs_body['last_name'])
    print('PASS Test case1: customers endpoint, pos, create customer.')
    print()

def test_verify_customer_in_db():
    '''

    :return:
    '''

    print('TC2, customers endpoint, pos, verify a customer in db.')


    customer_info = helper.get_customer_info_from_db_id_provided(customer_id=customer_id)

    print('Customer id: {}'.format(customer_id))
    # print('Customer_info:')
    # for k,v in customer_info.items():
    #     print('{}: {}'.format(k, v))

    assert customer_info['email'] == email, '"email" in response is not as expected. Expected: {}. Returned: {}.'.format(email, customer_info['email'])
    assert customer_info['nickname'] == username, '"username" in response is not as expected. Expected: {}. Returned: {}.'.format(username, customer_info['nickname'])
    assert customer_info['first_name'] == first_name, '"first_name" in response is not as expected. Expected: {}. Returned: {}.'.format(first_name, customer_info['first_name'])
    assert customer_info['last_name'] == last_name, '"last_name" in response is not as expected. Expected: {}. Returned: {}.'.format(last_name, customer_info['last_name'])
    print('PASS TC2, customers endpoint, pos, verify a customer in db.')






