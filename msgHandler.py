import re
import sys
from cmdHandler import Command

class Message:
    _tmi_regex = re.compile(r":\w+!\w+@\w+.tmi.twitch.tv")
    _cmd_regex = re.compile(r"!(\w+( \w+){0,3})")
    _usr_regex = re.compile(r"#(\w+)")
    _categories = ['PRIVMSG']

    def hasCommand(text):
        return(Message._cmd_regex.search(text) != None)

    def hasMeta(headers):
        # print(f"Headers: {headers}")
        return(len(headers.split(';')) > 0)

    def parse_message(message):
        msgObj = dict()
        try:
            headers, text = Message._tmi_regex.split(message)
            msgObj.update(Message.parse_channel(text))
            if Message.hasMeta(headers):
                msgObj.update(Message.parse_meta(headers))
            if Message.hasCommand(text):
                msgObj.update(Message.parse_command(text))
                msgObj.update(Message.command_director(msgObj))
        except ValueError as e:
            # Some messages don't have headers
            # print(f"Warn: Message.{'(parse_message)'}: {sys.exc_info()[1]}")
            pass
        except Exception as e:
            print(f"Error: Message.{'(parse_message)'}: {sys.exc_info()}")
            # sys.exc_info().print_exc()
            # print(f"{errno}\n{strerror}")
        finally:
            return(msgObj)

    def parse_channel(text):
        return({'channel': Message._usr_regex.search(text).group()[1:]})

    def parse_command(text):
        delim = '!'
        # commands[0] would have been ' PRIVMSG #xinthral :'
        return({'commands': [cmd.rstrip() for cmd in text.split(delim)[1:]]})

    def parse_meta(message):
        msg_dict = dict()
        try:
            for k,v in [record.split('=') for record in message.split(';')]:
                msg_dict[k] = v
        except Exception as e:
            print(f"Error: Message.{'(parse_meta)'}: {sys.exc_info()[1]}")
        finally:
            # print(f'Mdict: {msg_dict}')
            return(msg_dict)

    def command_director(message_object):
        """ Calls to the Command class """
        return(Command(message_object).parse())
