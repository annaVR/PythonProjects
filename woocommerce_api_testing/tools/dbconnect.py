import pymysql

class DBConnect():

    def __init__(self):
        pass

    def __connect(self, db):
        '''

        :param db:
        :return:
        '''
        host = '127.0.0.1'
        connection = pymysql.connect(host=host, port=3306, user='serega', password='foobar1', db=db)
        return connection

    def select(self, db, query):

        '''

        :param db:
        :param query:
        :return:
        '''

        connection = self.__connect(db)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        # print(result)

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))
            all_rows.append(row)

        connection.close()
        cursor.close()
        return all_rows


    def update(self, db, query):
        '''

        :param db:
        :param query:
        :return:
        '''
        host = '127.0.0.1'
        connection = self.__connect(db)
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()

        connection.close()
        cursor.close()

        return result






