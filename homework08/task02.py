import sqlite3 as sq


class TableData:
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.__cursor = self.__connect()

    def __connect(self):
        with sq.connect(self.database) as connect:
            connect.row_factory = sq.Row
            cursor = connect.cursor()
        return cursor

    def __len__(self):
        self.__cursor.execute('SELECT count(*) FROM {}'.format(self.table))
        return self.__cursor.fetchone()[0]

    def __getitem__(self, item):
        self.__cursor.execute(
            'SELECT * FROM {} WHERE name = "{}"'.format(self.table, item)
        )
        return tuple(self.__cursor.fetchone())

    def __contains__(self, item):
        self.__cursor.execute(
            'SELECT * FROM {} WHERE name = "{}"'.format(self.table, item)
        )
        return self.__cursor.fetchall()

    def __iter__(self):
        self.__cursor.execute('SELECT * FROM {}'.format(self.table))
        return self.__cursor
