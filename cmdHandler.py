from utils import cnf

class Commands:
    __authorized_commands = [cmd.strip() for cmd in cnf('ADMIN', 'AUTH_COMMANDS').split(',')]
    def __init__(self):
        print(Commands.__authorized_commands)
