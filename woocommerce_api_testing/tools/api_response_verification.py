__author__ = 'anna'

#was used in product_negative_test
def verify_positive_test_api_responce_correct(response, test_case_description, expected_info):

    if test_case_description.split('"')[1] == 'coupons':

        # exp_code, exp_amount, exp_individual_use, exp_exclude_sale_items, exp_minimum_amount = expected_info

        print(response)

        actual_info = response[1]['coupon']
        act_code = actual_info['code']
        # act_discount_type = actual_info['discount_type']
        act_amount = actual_info['amount']
        act_individual_use = actual_info['individual_use']
        act_exclude_sale_items = actual_info["exclude_sale_items"]
        act_minimum_amount = actual_info['minimum_amount']
        actual_info_list = [act_code, act_amount, act_individual_use, act_exclude_sale_items, act_minimum_amount]
        return actual_info_list == expected_info, 'Expected coupon info: {}. Actual coupon info: {}.'.format(expected_info, actual_info_list)




def verify_test_case_response(response,
                                       test_case_number,
                                       test_case_description,
                                       exp_error_msg=None,
                                       exp_error_code=None,
                                       expected_info=None):
    '''

    :return: verification result
    '''
    print('Running Test case {}: {}.'.format(test_case_number, test_case_description))
    actual_status_code = response[0]
    rs_body = response[1]
    if test_case_description.split(',')[0] == 'negative':
        expected_status_code = 400
        assert actual_status_code == expected_status_code, \
            'Test case {}: {}, Expected status_code: {}. Returned: {}'.format(test_case_number, test_case_description, expected_status_code, actual_status_code)


        assert 'errors' in rs_body.keys(), 'Test case {}: {}, no "errors" key in response body.'.format(test_case_number, test_case_description)

        # exp_error_msg = exp_error_msg
        act_error_msg = rs_body['errors'][0]['message']
        assert act_error_msg == exp_error_msg, 'Test case {}: {}, Expected error message: {}. ' \
                                               'Returned: {}'.format(test_case_number, test_case_description, exp_error_msg, act_error_msg)

        # exp_error_code = exp_error_code
        act_error_code = rs_body['errors'][0]['code']

        assert act_error_code == exp_error_code, 'Test case {}: {}, Expected code message: {}. ' \
                                               'Returned: {}'.format(test_case_number, test_case_description, exp_error_code, act_error_code)
        return 'Test case {}: {}. Result: PASS'.format(test_case_number, test_case_description)
    elif test_case_description.split(',')[0] == 'positive':
        expected_status_code = 201
        post_id = rs_body['coupon']['id']
        assert actual_status_code == expected_status_code, 'Test case {}: {}, Expected status_code: {}. Returned: {}'.format\
            (test_case_number, test_case_description, expected_status_code, actual_status_code)
        assert verify_positive_test_api_responce_correct(response, test_case_description, expected_info)
        return 'Test case {}: {} post_id: {}. Result: PASS'.format(test_case_number, test_case_description, post_id)





