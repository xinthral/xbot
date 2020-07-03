'''
Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at http://aws.amazon.com/apache2.0/
or in the "license" file accompanying this file.
This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
'''

import sys
import irc.bot
import re
import requests
import time
from apiHandler import *
from featuresExtended import *
from featuresHandler import *
from utils import *

CHAN = cnf('SERVER', 'CHANNEL')
NICK = cnf('AUTH', 'NICK')
TOKE = cnf('AUTH', 'ACCESS_TOKEN')
IDEN = cnf('AUTH', 'CLIENT_ID')

class NerdKommander(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/helix/users?login=' + channel
        self.headers = {
            'Client-ID': client_id,
            'Authorization': 'Bearer ' + self.token,
            'Accept': 'application/vnd.twitchtv.helix+json'
            }
        r = requests.get(url, headers=self.headers).json()
        print(r)

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
        CommandHandler(self, command)

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
            print("Bot: Added {} to ModList.".format(self.requestor))
        return

def main():
    if len(sys.argv) > 1:
        channel = sys.argv[1]
        #print("Usage: twitchbot <username> <client id> <token> <channel>")
        #sys.exit(1)
    else:
        channel = CHAN

    username  = NICK
    client_id = IDEN
    token     = TOKE

    try:
        bot = NerdKommander(username, client_id, token, channel)
        bot.start()
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
