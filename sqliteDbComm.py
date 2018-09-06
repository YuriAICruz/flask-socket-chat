import sqlite3


class SqLt:
    def __init__(self, sb_path):
        self.conn = sqlite3.connect(sb_path)
        print("Opened database successfully")

    def create_table(self, name, cols):
        q = ' ('

        for i in range(0, len(cols)):
            q = q + cols[i][0] + " " + cols[i][1]
            if i < len(cols) - 1:
                q = q + ", "

        q = q + ')'

        self.conn.execute('CREATE TABLE IF NOT EXISTS ' + name + q)

    def drop_table(self, name):
        self.conn.execute('DROP TABLE IF EXISTS ' + name)

    def append(self, table, data):
        try:
            qb = '('

            for i in range(0, len(data)):
                qb = qb + "'" + data[i][1] + "'"
                if i < len(data) - 1:
                    qb = qb + ", "

            qb = qb + ')'

            q = ' ('

            for i in range(0, len(data)):
                q = q + data[i][0]
                if i < len(data) - 1:
                    q = q + ", "

            q = q + ')'

            query = 'INSERT INTO ' + table + q + " VALUES" + qb

            self.conn.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)

    def close(self):
        self.conn.close()
        print("Closed database successfully")
