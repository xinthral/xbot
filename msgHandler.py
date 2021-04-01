import re
import sys
from featuresHandler import CommandHandler

class Message:
    _tmi_regex = re.compile(r":\w+!\w+@\w+.tmi.twitch.tv")
    _cmd_regex = re.compile(r"!\w+( \w+){0,3}")
    _usr_regex = re.compile(r"#(\w+)")

    def parse_message(message):
        msgObj = dict()
        try:
            if Message._tmi_regex.search(message):
                matches = re.split(Message._tmi_regex, message)
                if matches[0] != None:
                    msgObj = Message.parse_meta(matches[0])
                if Message._cmd_regex.search(message) != None:
                    msgObj['text'] = matches[1]
                    msgObj['channel'] = Message._usr_regex.search(msgObj['text']).group(0)[1:]
                    msgObj['commands'] = Message.parse_command(matches[1])
                    # print(f"Channel set to {msgObj['channel']}")
        except TypeError:
            print(f"Warn: Message.{'(parse_message)'} received a blank message.")
            pass
        except Exception as e:
            print(f"Error: Message.{'(parse_message)'}: {sys.exc_info()}")
            pass
        finally:
            return(msgObj)

    def parse_command(message):
        output = []
        try:
            commands = Message._cmd_regex.search(message).group(0)
            print('CommandTest: ')
            print(commands)
            for command in message.split('!')[1:]:
                command = command.split(' ')
                output.append(command)
            return(output)
        except Exception as e:
            print(f"Error: Message.{'parse_command'} recieved and exception.")
        
    def parse_meta(message):
        msg_dict = dict()
        try:
            for k,v in [record.split('=') for record in message.split(';')]:
                msg_dict[k] = v
        except Exception as e:
            print(f"Error: Message.{'(parse_meta)'}: {sys.exc_info()}")
        finally:
            return(msg_dict)
