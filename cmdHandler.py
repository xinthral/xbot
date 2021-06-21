from db.xsql import Database
from commands.features import Skits
from utils import cnf

class Command:
    # This should be converted to a settings SQL db
    _authorized_commands = [cmd.strip() for cmd in cnf('ADMIN', 'AUTH_COMMANDS').split(',')]
    _delim = cnf('ADMIN', 'DELIM')
    _options = ['add', 'list', 'search']

    def __init__(self, message_object):
        self.obj = message_object
        self.skit = Skits()

    def parse(self):
        resp = list()
        for cmd in self.obj['commands']:
            output = self.response(cmd)
            resp.append(output)
        return({'response': resp})

    def response(self, commandline):
        response = list()
        cmdline = commandline.split()
        cmd = cmdline[0].lower()
        if cmd not in Command._authorized_commands:
            # response = ['Invalid Command']
            pass
        else:
            if cmd in Database._tables:
                # response = self.joke_parse(cmdline).split(Command._delim)
                response = self.skit.get_response(cmd)
            elif cmd == 'quote' or cmd == 'phrase':
                # response = ['this is a temp quote', 'cause temp quote are needed', 'for testing']
                # response = self.phrase_parse(cmdline).split(Command._delim)
                pass
            elif cmd == 'fact':
                # response = (facts(),)
                pass
            elif cmd == 'rather':
                # response = (' ',)
                pass
            else:
                response = ['Command: WUT']
        return(response)
