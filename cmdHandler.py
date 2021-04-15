from db.xsql import Database
from commands.features import jokes, quotes
from utils import cnf

class Command:
    # This should be converted to a settings SQL db
    _authorized_commands = [cmd.strip() for cmd in cnf('ADMIN', 'AUTH_COMMANDS').split(',')]
    _delim = cnf('ADMIN', 'DELIM')
    _options = ['add', 'list', 'search']

    def __init__(self, message_object):
        self.obj = message_object

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
            response = ['Invalid Command']
        else:
            if cmd == 'joke':
                response = self.joke_parse(cmdline).split(Command._delim)
            elif cmd == 'quote' or cmd == 'phrase':
                # response = ['this is a temp quote', 'cause temp quote are needed', 'for testing']
                response = self.phrase_parse(cmdline).split(Command._delim)
            else:
                response = ['Command: WUT']
        return(response)

    def joke_parse(self, commandline):
        response = tuple()
        if len(commandline) > 1:
            response = jokes(commandline[1])
        else:
            response = jokes('dad')
        # print(f'Joke Parse Resp: {response}')
        return(response[1])

    def phrase_parse(self, commandline):
        response = tuple()
        if len(commandline) > 1:
            response = quotes(commandline[1])
        else:
            response = quotes('positivity')
        # print(f'Quote Parse Resp: {response}')
        return(response[1])
