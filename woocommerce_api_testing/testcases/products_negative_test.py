import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/woocommerce_api_testing')

from tools import request

rq = request.Request()

def verify_negative_test_case_response(response, test_case_number, test_case_description, exp_error_msg, exp_error_code):
    '''

    :return:
    '''
    print('Running Test case {}: {}.'.format(test_case_number, test_case_description))
    rs_code = response[0]
    assert rs_code == 400, 'Test case {}: {}, Expected status_code: {}. Returned: {}'.format(test_case_number, test_case_description, 400, rs_code)

    rs_body = response[1]
    assert 'errors' in rs_body.keys(), 'Test case {}: {}, no "errors" key in response body.'.format(test_case_number, test_case_description)

    exp_error_msg = exp_error_msg
    act_error_msg = rs_body['errors'][0]['message']
    assert act_error_msg == exp_error_msg, 'Test case {}: {}, Expected error message: {}. ' \
                                           'Returned: {}'.format(test_case_number, test_case_description, exp_error_msg, act_error_msg)

    exp_error_code = exp_error_code
    act_error_code = rs_body['errors'][0]['code']

    assert act_error_code == exp_error_code, 'Test case {}: {}, Expected code message: {}. ' \
                                           'Returned: {}'.format(test_case_number, test_case_description, exp_error_code, act_error_code)
    return 'Test case {}: {} PASS'.format(test_case_number, test_case_description)

def test_ng_tc1_product_empty_payload():
    '''

    :return:
    '''
    print('Running Test case 1: testing "products" endpoint, payload is empty json.')

    input_data = {}
    rs = rq.post('products', input_data)

    # print(rs)

    rs_code = rs[0]
    assert rs_code == 400, 'Test case 1: empty payload, Expected status_code: {}. Returned: {}'.format(400, rs_code)

    rs_body = rs[1]
    assert 'errors' in rs_body.keys(), 'Test case 1: empty payload, no "errors" key in response body.'

    exp_error_msg = 'No product data specified to create product'
    act_error_msg = rs_body['errors'][0]['message']
    assert act_error_msg == exp_error_msg, 'Test case 1: empty payload, Expected error message: {}. ' \
                                           'Returned: {}'.format(exp_error_msg, act_error_msg)
    exp_error_code = 'woocommerce_api_missing_product_data'
    act_error_code = rs_body['errors'][0]['code']

    assert act_error_code == exp_error_code, 'Test case 1: empty payload, Expected code message: {}. ' \
                                           'Returned: {}'.format(exp_error_code, act_error_code)

    print('Test case 1: Empty payload PASS')

def test_ng_tc2_product_missing_title_key_in_payload():
    '''

    :return:
    '''

    print('Running Test case 2: testing "products" endpoint, missing title key in payload.')

    input_data = {}
    product = {}
    product['type'] = 'simple'
    product['regular_price'] = '9.99'
    input_data['product'] = product

    rs = rq.post('products', input_data)

    rs_code = rs[0]
    assert rs_code == 400, 'Test case 2: missing "title" key in payload, Expected status_code: {}. Returned: {}'.format(400, rs_code)

    rs_body = rs[1]
    assert 'errors' in rs_body.keys(), 'Test case 2: missing "title" key in payload, no "errors" key in response body.'

    exp_error_msg = 'Missing parameter title'
    act_error_msg = rs_body['errors'][0]['message']
    assert act_error_msg == exp_error_msg, 'Test case 2: missing "title" key in payload, Expected error message: {}. ' \
                                           'Returned: {}'.format(exp_error_msg, act_error_msg)
    exp_error_code = 'woocommerce_api_missing_product_title'
    act_error_code = rs_body['errors'][0]['code']

    assert act_error_code == exp_error_code, 'Test case 2: missing "title" key in payload, Expected code message: {}. ' \
                                           'Returned: {}'.format(exp_error_code, act_error_code)

    print('Test case 2: missing "title" key payload PASS')

def test_ng_tc3_empty_string_for_title_in_payload():
    '''

    :return:
    '''

    test_case_number = 3
    test_case_description = 'ng, "products" endpoint, empty string for title in payload'

    input_data = {}
    product = {}
    product['type'] = 'simple'
    product['regular_price'] = '9.99'
    product['title'] = ''
    input_data['product'] = product

    rs = rq.post('products', input_data)
    # print(rs)
    exp_error_msg = 'Content, title, and excerpt are empty.'
    exp_error_code = 'woocommerce_api_cannot_create_product'

    print(verify_negative_test_case_response(rs, test_case_number, test_case_description, exp_error_msg, exp_error_code))

def test_ng_tc4_random_string_for_input():
    '''

    :return:
    '''
    test_case_number = 4
    test_case_description = 'ng, "products" endpoint, random string for input'

    input_data = 'jkdfhsnaf89'
    rs = rq.post('products', input_data)
    # print(rs)
    exp_error_msg = 'No product data specified to create product'
    exp_error_code = 'woocommerce_api_missing_product_data'
    try:
        print(verify_negative_test_case_response(rs, test_case_number, test_case_description, exp_error_msg, exp_error_code))
    except:
        print('Test case {}: {} FAILED'.format(test_case_number, test_case_description))




test_ng_tc1_product_empty_payload()
test_ng_tc2_product_missing_title_key_in_payload()
test_ng_tc3_empty_string_for_title_in_payload()

# the tc4 found the bag - wrong error message and wrong error code
test_ng_tc4_random_string_for_input()