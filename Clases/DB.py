import pymysql
class db():


    @staticmethod
    def connect(query):
        db=pymysql.connect(host = '127.0.0.1',user = 'root',passwd='alumno',db='mydb',charset = 'utf8',autocommit = True)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        db.close()
        return cursor