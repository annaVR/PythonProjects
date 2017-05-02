import sys
sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/woocommerce_api_testing')

from datetime import datetime
import string
import random
from tools import dbconnect

class Helper():

    def __init__(self):
        pass
    qrq = dbconnect.DBConnect()

    def generate_customer_info(self):
        '''
        The helper to generate random customer info: email, username, name, last name.
        :return:
        '''

        customer_info = {}
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        customer_info['email'] = 'api_user_' + timestamp + '@gmail.com'
        customer_info['username'] = 'backend.' + timestamp

        all_letters = string.ascii_lowercase
        customer_info['first_name'] = ''.join(random.sample(all_letters, 8)).capitalize()
        customer_info['last_name'] = ''.join(random.sample(all_letters, 8)).capitalize()
        return customer_info

    def generate_coupon_info(self):
        '''
        This helper will generate random coupon info
        :return: code, discount_type, amount, minimum_amount
        '''

        
        amount = str(random.randrange(5, 95, 5))
        code = amount + 'off'
        # discount_type = 'percent'


        individual_use = True
        exclude_sale_items = True
        minimum_amount = str(float(random.randrange(50, 150, 10)))
        coupon_info = [code, amount, individual_use, exclude_sale_items, minimum_amount]
        # coupon_info['code'] = code
        # coupon_info['discount_type'] = discount_type
        # coupon_info['amount'] = amount
        # coupon_info['individual_use'] = True
        # coupon_info['exclude_sale_items'] = True
        # coupon_info['minimum_amount'] = minimum_amount


        return coupon_info

    def get_customer_info_from_db_id_provided(self, customer_id):

        '''

        :param customer_id:
        :return:
        '''

        customer_info = dict()
        query_1 = 'select user_login, user_email, ID from wp179.ms_users where ID={}'.format(customer_id)
        customers = self.qrq.select('wp179', query_1)
        customer_info['user_name'] = customers[0][0]
        customer_info['email'] = customers[0][1]
        customer_info['id'] = customers[0][2]

        query_2 = 'select meta_key, meta_value from wp179.ms_usermeta where user_id={}'.format(customer_id)
        customers_meta = self.qrq.select('wp179', query_2)
        for row in customers_meta:
            customer_info[row[0]] = row[1]

        return(customer_info)

    def get_coupon_codes_from_db(self):
        '''

        :return: the list of coupon codes existing in db
        '''

        query = "select post_name from wp179.ms_posts where post_type='shop_coupon'"
        coupon_codes = self.qrq.select('wp179', query)
        coupon_codes_list = []
        for item in coupon_codes:
            coupon_codes_list.append(*item)
        return coupon_codes_list






