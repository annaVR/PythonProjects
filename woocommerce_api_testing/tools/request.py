from woocommerce import API

class Request():

    def __init__(self):

        admin_consumer_key = 'ck_4e5935f19c74e13c2ae54df112cc102038296de8'
        admin_consumer_secret = 'cs_83fea685b8d35aef74847024fc14636cfdb4121c'

        self.wcapi = API(
            url='http://127.0.0.1/my_store',
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            version='v2')

    def test_api(self):
        '''

        :return:
        '''
        print(self.wcapi.get('').json())
        print(self.wcapi.get('').status_code)

    def post(self, endpoint, data):
        '''

        :param endpoint:
        :param data:
        :return:
        '''

        responce = self.wcapi.post(endpoint, data)
        rs_code = responce.status_code
        rs_body = responce.json()
        rs_url = responce.url

        return [rs_code, rs_body, rs_url]

    def get(self, endpoint):
        '''
        :param endpoint:
        :return:
        '''

        responce = self.wcapi.get(endpoint)
        rs_code = responce.status_code
        rs_body = responce.json()
        rs_url = responce.url

        return [rs_code, rs_body, rs_url]
