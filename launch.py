import irc.bot
import json
import requests
import sys

from utils import cnf

class xBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, username, client_id, token):
        self.username = username
        self.client_id = client_id
        self.token = token
        self.channel = channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/helix/users?login=' + channel
        self.headers = {'Client-ID': client_id,
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/vnd.twitchtv.helix+json',
        }
        r = requests.get(url, headers=self.headers).json()
        print(r)

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self,
            [(server, port, 'oauth:' + token)],
            username, username)
    pass

def main():
    if len(sys.argv) > 1:
        channel = sys.argv[1]
        print("Usage: twitchbot <channel> <username> <client id> <token>")
        #sys.exit(1)
    else:
        channel = cnf('AUTH', 'CHANNEL_ID')

    username  = cnf('AUTH', 'IDENT')
    client_id = cnf('AUTH', 'CLIENT_ID')
    token     = cnf('AUTH', 'ACCESS_TOKEN')

    try:
        bot = xBot(channel, username, client_id, token)
        bot.start()
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
