import re
import sys
from cmdHandler import Command

class Message:
    _cmd_regex = re.compile(r"!(\w+)( \w+){0,3}")
    _mod_regex = re.compile(r":(\w+)\.tmi\.twitch\.tv \d+ \w+ = #(\w+) :(.*)")
    _msg_regex = re.compile(r":(\w+)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)")
    _tmi_regex = re.compile(r":(\w+)\!.*@.*\.tmi\.twitch\.tv ([A-Z]+) #(\w+)")
    # _events = ['PRIVMSG', 'USERSTATE', 'ROOMSTATE', 'JOIN', 'PART', 'PING', 'CAP * ACK', 'HOSTTARGET', 'HOST']

    def parse_message(message):
        """ Parse all incoming messages """
        response_obj = dict()
        if message.startswith(':'):
            response_obj.update(Message._parse_notification(message))
        elif message.startswith('@'):
            response_obj.update(Message._parse_privmsg(message))
        elif message.startswith('PING'):
            response_obj.update(Message._ping_response())
        else:
            pass
        # elif message.startswith('.'):
        # elif message.startswith('='):
        return(response_obj)

    def _parse_headers(message):
        """ Parse Meta Data """
        meta = message.split(' :')
        response_obj = dict([ele.split('=') for ele in meta[0].split(';')])
        return(response_obj)

    def _parse_notification(message):
        """ Parse incoming notification messages """
        response_obj = dict()

        # Handles Join/Part Events
        if Message._tmi_regex.search(message) != None:
            response_obj['username'], response_obj['category'], response_obj['channel'] = Message._tmi_regex.search(message).groups()

        # Handles Modlist Response
        elif Message._mod_regex.search(message) != None:
            response_obj['username'], response_obj['channel'], mods = Message._mod_regex.search(message).groups()
            response_obj['mods'] = mods.split(' ')

        # else:
            # Message: _':tmi.twitch.tv HOSTTARGET #xinthral :arcangl -'_
            # Message: _':tmi.twitch.tv CAP * ACK :twitch.tv/membership'_
            # Message: _':tmi.twitch.tv CAP * ACK :twitch.tv/tags'_
            # Message: _':tmi.twitch.tv CAP * ACK :twitch.tv/commands'_
            # Message: _':nerd_kommander.tmi.twitch.tv 366 nerd_kommander #nerd_kommander :End of /NAMES list'_

        return(response_obj)

    def _parse_privmsg(message):
        """ Serialize raw message into object """
        response_obj = dict({'response': []})
        response_obj.update(Message._parse_headers(message))

        # Handles PRIVMSG Events
        if Message._msg_regex.search(message) != None:
            response_obj['username'], response_obj['channel'], response_obj['text'] = Message._msg_regex.search(message).groups()
            """

            PUT SOME SHIT HERE TO DO THINGS

            """
            # print(f"Text: {response_obj['text']}")
            # response_obj['response'].append(f"{len(response_obj['text'])}")
        # else:
            # Message: _'@msg-id=host_on :tmi.twitch.tv NOTICE #xinthral :Now hosting ArcAngL.'_

        return(response_obj)

    def _ping_response():
        return({'response': 'PONG'})

    def command_director(command):
        """ Calls to the Command class """
        pass
        # return(Command(command).parse())
