import sys
from utils import cnf
from xBot import NerdKommander

def main():
    if len(sys.argv) > 1:
        channel = sys.argv[1]
        print("Usage: twitchbot <channel> <username> <client id> <token>")
        #sys.exit(1)
    else:
        channel = cnf('AUTH', 'CHANNEL_ID')

    username  = cnf('AUTH', 'NICK')
    client_id = cnf('AUTH', 'CLIENT_ID')
    token     = cnf('AUTH', 'ACCESS_TOKEN')

    try:
        bot = NerdKommander(channel, username, client_id, token)
        bot.start()
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
