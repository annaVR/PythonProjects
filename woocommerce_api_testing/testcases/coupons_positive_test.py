__author__ = 'anna'

import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/woocommerce_api_testing')

from tools import request
from tools import helpers
from tools import api_response_verification

import json

rq = request.Request()
helper = helpers.Helper()

def test_create_a_coupon():

    global code
    global discount_type
    global amount
    global minimum_amount
    global individual_use
    global exclude_sale_items
    global response

    test_case_number = 1
    test_case_description = 'positive, "coupons" endpoint, create a coupon with valid payload.'

    #verify that coupon_code not in db
    coupon_codes_in_db = helper.get_coupon_codes_from_db()
    code_in_db = True
    while code_in_db is True:
        coupon_info = helper.generate_coupon_info()
        code, amount, individual_use, exclude_sale_items, minimum_amount = coupon_info
        if code not in coupon_codes_in_db:
            code_in_db = False

    data = {}
    data['coupon'] = {
    "code": code,
    "amount": amount,
    "individual_use": individual_use,
    "exclude_sale_items": exclude_sale_items,
    "minimum_amount": minimum_amount}
    print(data)

    response = rq.post('coupons', data)
    print(response)
    # #remove discount_type from coupon_info, since we do not need it:
    # coupon_info.remove(individual_use)
    print(api_response_verification.verify_test_case_response(response,
                                       test_case_number,
                                       test_case_description,
                                       coupon_info
                                      ))
test_create_a_coupon()


# def test_verify_coupon_in_database(coupon_id):



# response = rq.get('customers')
# response_code = response[0]
# response_body = response[1]
# customers = response_body['customers']
# print(len(customers))
# for item in customers:
#     print(item['id'], json.dumps(item, indent=4))



