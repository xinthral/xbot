import sys
import irc.bot
import re
import requests
import time
import threading
from apiHandler import *
from featuresExtended import *
from featuresHandler import *
from utils import *

class NerdKommander(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for new API calls
        url = 'https://api.twitch.tv/helix/users?login=' + channel
        self.headers = {
            'Accept': 'application/vnd.twitchtv.helix+json',
            'Authorization': f'Bearer {self.token}',
            'Client-ID': self.client_id,
            }
        r = requests.get(url, headers=self.headers)
        if r.status_code != 200:
            sys.exit(0)
        else:
            r = r.json()

        # Generate Permissions List
        self.admins = cnf('ADMIN', 'ADMINS').split(', ')
        for usr in cnf('ADMIN', 'OWNERS').split(', '):
            self.admins.append(usr)
        self.channel_id = r['data'][0]['login']
        if self.channel_id.lower() not in self.admins:
            self.admins.append(self.channel_id)
        self.moderators = self.admins
        for usr in tmi_chatters(self.channel_id)['chatters']['moderators']:
            if usr not in self.moderators:
                self.moderators.append(usr)

        # Establish Class Variables
        self.channel_idNumber = r['data'][0]['id']
        self.channel_displayName = r['data'][0]['display_name']
        self.commandList = cnf('ADMIN', 'AUTH_COMMANDS').split(', ')

        # Dev Configurations
        self.allowedJokes = cnf('ADMIN', 'AUTH_JOKES').split(', ')
        self.regex = r"!\w+( \w+){0,3}"
        self.debug = cnf('DEV', 'DEBUG')

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, f'oauth:{token}')],
                                            username, username)

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)
        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # If a chat message starts with an exclamation point,
        # try to run it as a command
        match = re.search(self.regex, e.arguments[0])
        if match != None:
            command = match.group()[1:].strip().split(' ')
            self.parseTags(e.tags)
            #FIXME: Logging Line
            print(f'{self.requestor} requested {command[0]}')

            if self.requestor.lower() in self.moderators and command[0].lower() in self.commandList:
                self.do_command(command)
            else:
                pass
        return

    @Logr
    def do_command(self, command):
        t1 = threading.Thread(target=CommandHandler, args=(self, command))
        t1.start()
        # CommandHandler(self, command)

    def parseTags(self, tags):
        isMod = 0
        for element in tags:
            if element['key'] == 'display-name':
                self.requestor = element['value']
            if element['key'] == 'mod':
                isMod = int(element['value'])

        # If requestor is a mod and not known, add to known moderator list.
        if isMod == 1 and self.requestor.lower() not in self.moderators:
            self.moderators.append(self.requestor.lower())
            print(f'Bot: Added {self.requestor} to ModList.')
        return
