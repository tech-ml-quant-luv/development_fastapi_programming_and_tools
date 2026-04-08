import psycopg2

class DbConnection:

    def __init__(self,host="localhost",dbname="postgres", user="postgres", password="987654321", port=5432):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.cur = self.conn.cursor()


    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()