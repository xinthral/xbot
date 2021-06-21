"""
Command Line Interface for SQLite Databases
"""
from xsql import Database

def display_detailed_record(item_id, table):
    """ Given a database tuple response, outputs formatted for readability """
    divider = "\t..::--== ==--::.."
    item = Database.queryTableID(item_id, table)
    print(divider)
    print(f"{'Visible':8}: {('Yes' if str(item[3]) == '0' else 'No')}")
    print(f"{'Category':8}: {item[2]}")
    count = 1
    for line in item[1].split(Database._delim):
        print(f"Line {count} :: {line}")
        count += 1
    print(divider)
    pause()

def flipVisibility(item_id, table):
    """ Change the visibility boolean in the database """
    current = Database.queryTableID(item_id, table)
    flipped = 1 if str(current[3]) == '0' else 0
    # table, column, value, pid
    Database.updateVisibility((table, 'isBlocked', int(flipped), int(item_id)))
    pause()

def get_database_choice():
    """ Retrieve User choice on database menu """
    choice = input('What table do you want to interact with?: ')
    if choice.lower().strip() == 'q': return(False)
    if (validate_database_choice(choice)):
        return(choice)
    else:
        return(get_database_choice())

def get_table_choice(menu):
    """ Retrieve User choice on table menu """
    choice = input('Choose an option (q to quit): ')
    if choice.lower().strip() == 'q': return(False)
    if (validate_table_choice(choice, menu.keys())):
        return(choice)
    else:
        return(get_table_choice(menu))

def interactive_table(table, item_id, choice):
    """ Handle Execution of table choice """
    print(f"SELECT * FROM {table} WHERE PID={item_id} WITH OPTION {choice}")
    if choice == '1':
        display_detailed_record(item_id, table)
    else:
        print('Womp Womp!')

def pause():
    """ Pause Console Script awaiting user input """
    paused = input('Enter to continue...')

def print_database_menu():
    """ Display current database tables """
    print(f"Tables: {Database._tables}")
    return(get_database_choice())

def print_table(table):
    """ Given a table name, print out formatted contents """
    print('Database output begins...')
    print(f"{'ID':4} || {'Off':3} || {'Category':16} || {'Content'}")
    for element in Database.queryTableAll(table):
        print(f"{element[0]:4} || {element[3]:3} || {element[2]:16} || {element[1]}")
    print('Database output complete...')

def print_table_menu():
    """ Display Menu Items """
    menu = {
        '1': 'Display a record in more readable formats',
        '2': 'Enable / Disable a record',
        '3': 'Change category of record',
        '4': 'Insert record into table',
        '5': 'Remove record from table',
    }
    print('Table Menu:')
    for k,v in menu.items():
        print(f" {k:2} :: {v}")
    return(get_table_choice(menu))

def validate_database_choice(choice):
    """ Returns a boolean if choice is a valid option """
    if (choice.lower().strip() not in Database._tables):
        print('Invalid Choice, try again.')
        return(False)
    else:
        return(True)

def validate_table_choice(choice, menu):
    """ Returns a boolean if choice is a valid option """
    if (choice not in menu):
        print('Invalid Choice, try again.')
        return(False)
    else:
        return(True)

def main():
    repeat = True
    table = None
    while (repeat):
        dbs_choice = print_database_menu()
        if dbs_choice != False:
            print_table(dbs_choice)
            item_id = input('What record (id) would you like to interact with?: ')
            tbl_choice = print_table_menu()
            if tbl_choice != False:
                interactive_table(dbs_choice, item_id, tbl_choice)
        usr_choice = input('Do you wish to continue? [Y/n]: ')
        repeat = True if usr_choice.lower() == 'y' else False

if __name__ == '__main__':
    main()
