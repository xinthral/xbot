import sqlite3
from os import getcwd

class Database:
    _delim = ';::;'
    _library = 'library.db'
    _tables = ['jokes', 'phrases']

    def create_connection(db_file=_library):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            raise(e)
        return(conn)

    def queryTableAll(tbl_name=_tables[0]):
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"SELECT * FROM {tbl_name}")
        rows = c.fetchall()
        con.close()
        return(rows)

    def getTableSchema(tbl_name=_tables[0]):
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"PRAGMA table_info({tbl_name})")
        rows = c.fetchall()
        con.close()
        return(rows)

    def getTableHeaders(tbl_name=_tables[0]):
        return([ele[1] for ele in Database.getTableSchema(tbl_name)])

    def insertJoke(payload, tbl_name=_tables[0], delim=_delim):
        if len(payload[0].split(delim)) < 1:
            print('Empty Payload')
            return(False)

        columns = tuple(Database.getTableHeaders())
        con = Database.create_connection()
        c = con.cursor()
        elements = (Database.getTableCount(tbl_name), *payload, )
        print(elements)
        c.execute(f'''INSERT INTO {tbl_name} {columns} VALUES {elements}''')
        con.commit()
        con.close()
        return(True)

    def showTables():
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        rows = c.fetchall()
        con.close()
        return(rows)

    def getTableCount(tbl_name=_tables[0]):
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f'SELECT COUNT(*) FROM {tbl_name}')
        count = c.fetchone()[0]
        con.close()
        return(count)
