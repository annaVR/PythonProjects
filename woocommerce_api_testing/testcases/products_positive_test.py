# import sys
# sys.path.insert(0, '/home/anna/PycharmProjects/PythonProjects/woocommerce_api_testing')

from ..tools import dbconnect
from ..tools import request
import json
req = request.Request()
qry = dbconnect.DBConnect()

def test_create_a_product():
    '''

    :return:
    '''

    global product_id
    global title
    global price

    title = 'Test1 title'
    price = '9.99'

    input_data = {
        'product':{
        'title': title,
        'type': 'simple',
        'regular_price': price
    }}

    rs = req.post('products', input_data)

    # print()
    # for item in info:
    #     print(json.dumps(item, indent=4))

    rs_code = rs[0]
    rs_body = rs[1]

    rs_title = rs_body['product']['title']
    rs_price = rs_body['product']['regular_price']
    product_id = rs_body['product']['id']

    assert rs_code == 201, 'The returned status code is not as expected.' \
                           'Expected: 201. Returned: {}'.format(rs_code)


    assert rs_title == title, 'The returned title is not as expected.' \
                              'Expected: {}. Returned: {}'.format(title, rs_title)

    assert rs_price == price, 'The return regular price is not as expected.' \
                              'Expected: {}. Returned: {}'.format(price, rs_price)

    print('id: {}'.format(product_id))
    print('The create_product test PASS.')

def test_verity_product_created_in_db():
    '''

    :return:
    '''

    query = ''' select p.post_title, p.post_type, pm.meta_value
    from ms_posts p join ms_postmeta pm on p.ID=pm.post_id where p.ID ={}
    and pm.meta_key='_regular_price' '''.format(product_id)

    qrs = qry.select('wp179', query)

    print(qrs)

    db_title = qrs[0][0]
    db_type = qrs[0][1]
    db_regular_price = qrs[0][2]


    assert db_title == title, 'The returned title is not as expected.' \
                              'Expected: {}. Returned: {}'.format(title, db_title)
    assert db_type == 'product', 'The post_type returned is not as expected.' \
                                 'Expected: {}. Returned: {}'.format('product', db_type)
    assert db_regular_price == price, 'The price returned is not as expected.' \
                                      'Expected: {}. Returned: {}'.format(price, db_regular_price)

    print('Product positive tc, verify product created in db, PASS')

test_create_a_product()
test_verity_product_created_in_db()
