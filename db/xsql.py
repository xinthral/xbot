import sqlite3
from os import getcwd

class Database:
    """ Static Class Scope Variables """
    _delim = ';::;'
    _library = 'db/library.db'
    _tables = ['facts', 'fortunes', 'jokes', 'quotes', 'rathers']

    def create_connection(db_file=_library):
        """ Establish Connection to database object and return connection object """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            raise(e)
        return(conn)

    def insert(payload, tbl_name=_tables[0], delim=_delim):
        if len(payload[0].split(delim)) < 1:
            print('Empty Payload')
            return(False)

        columns = tuple(Database.queryTableHeaders(tbl_name))
        con = Database.create_connection()
        c = con.cursor()
        elements = (Database.queryTableCount(tbl_name), *payload, )
        c.execute(f'''INSERT INTO {tbl_name} {columns} VALUES {elements}''')
        con.commit()
        con.close()
        return(True)

    def insertFact(payload):
        """ Inserts fact payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'facts'))

    def insertFortune(payload):
        """ Inserts fortune payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'fortunes'))

    def insertJoke(payload):
        """ Inserts joke payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'jokes'))

    def insertQuotes(payload):
        """ Inserts quotes payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'quotes'))

    def insertRather(payload):
        """ Inserts would you rather payload into database object (wrapper) """
        #payload: ['input text', 'category', blocked: 0/1]
        return(Database.insert(payload, 'rather'))

    def queryTableAll(tbl_name=_tables[0]):
        """ Query all items from a specific database in the database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"SELECT * FROM {tbl_name}")
        rows = c.fetchall()
        con.close()
        return(rows)

    def queryTableCategory(tbl_name=_tables[0], cat='dad'):
        """
        Query all elements for a specific category from a table in the database object
        """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"SELECT * FROM {tbl_name} WHERE category=\'{cat}\'")
        rows = c.fetchall()
        con.close()
        return(rows)

    def queryTableCount(tbl_name=_tables[0]):
        """ Query item count from a specific table in database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f'SELECT COUNT(*) FROM {tbl_name}')
        count = c.fetchone()[0]
        con.close()
        return(count)

    def queryTableHeaders(tbl_name=_tables[0]):
        """ Query Headers for specific table in database object """
        return([ele[1] for ele in Database.showTableSchema(tbl_name)])

    def queryTableID(item_id=0, tbl_name=_tables[0]):
        """ Query a specific items ID from a specific database in the database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"SELECT * FROM {tbl_name} WHERE pid={item_id}")
        item = c.fetchone()
        con.close()
        return(item)

    def queryTableVisible(tbl_name=_tables[0]):
        """ Query all items, filter by only records marked visible """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"SELECT * FROM {tbl_name} WHERE isBlocked={0}")
        rows = c.fetchall()
        con.close()
        return(rows)

    def showTables():
        """ Query table names from database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        rows = c.fetchall()
        con.close()
        return(rows)

    def showTableSchema(tbl_name=_tables[0]):
        """ Query Schema for specific table in database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"PRAGMA table_info({tbl_name})")
        rows = c.fetchall()
        con.close()
        return(rows)
