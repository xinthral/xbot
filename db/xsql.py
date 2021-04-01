import sqlite3
from os import getcwd

class Database:
    """ Static Class Scope Variables """
    _delim = ';::;'
    _library = 'db/library.db'
    _tables = ['jokes', 'phrases']

    def create_connection(db_file=_library):
        """ Establish Connection to database object and return connection object """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            raise(e)
        return(conn)

    def queryTableAll(tbl_name=_tables[0]):
        """ Query all items from a specific database in the database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"SELECT * FROM {tbl_name}")
        rows = c.fetchall()
        con.close()
        return(rows)

    def getTableSchema(tbl_name=_tables[0]):
        """ Query Schema for specific table in database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f"PRAGMA table_info({tbl_name})")
        rows = c.fetchall()
        con.close()
        return(rows)

    def getTableHeaders(tbl_name=_tables[0]):
        """ Query Headers for specific table in database object """
        return([ele[1] for ele in Database.getTableSchema(tbl_name)])

    def insert(payload, tbl_name=_tables[0], delim=_delim):
        if len(payload[0].split(delim)) < 1:
            print('Empty Payload')
            return(False)

        columns = tuple(Database.getTableHeaders(tbl_name))
        con = Database.create_connection()
        c = con.cursor()
        elements = (Database.getTableCount(tbl_name), *payload, )
        print(elements)
        c.execute(f'''INSERT INTO {tbl_name} {columns} VALUES {elements}''')
        con.commit()
        con.close()
        return(True)

    def insertJoke(payload):
        """ Inserts phrase payload into database object (wrapper) """
        return(Database.insert(payload, 'jokes'))

    def insertPhrase(payload):
        """ Inserts phrase payload into database object (wrapper) """
        return(Database.insert(payload, 'phrases'))

    def showTables():
        """ Query table names from database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        rows = c.fetchall()
        con.close()
        return(rows)

    def getTableCount(tbl_name=_tables[0]):
        """ Query item count from a specific table in database object """
        con = Database.create_connection()
        c = con.cursor()
        c.execute(f'SELECT COUNT(*) FROM {tbl_name}')
        count = c.fetchone()[0]
        con.close()
        return(count)

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

# DEFUNC
# """ HELPER FUNCTIONS """
# def convertJokesDict(category='dad'):
#     """ Converts the jokes dictionary into formmated joke for database object """
#     from jokes_db import jokesDict as jlist
#     rejected = []
#     db = Database
#     for joke in jlist[category]:
#         try:
#             joke = ';::;'.join(joke)
#             db.insertJoke([joke, category, False])
#         except Exception as ee:
#             rejected.append((joke, ee))
#     return(rejected)
#
# def convertPhraseDict(category='positivity'):
#     """ Converts the phrases dictionary into formmated phrase for database object """
#     from phrases_db import phraseDict as plist
#     rejected = []
#     db = Database
#     for phrase in plist[category]:
#         try:
#             phrase = ';::;'.join(phrase)
#             db.insertPhrase([phrase, category, False])
#         except Exception as ee:
#             rejected.apppend((phrase, ee))
#     return(rejected)
