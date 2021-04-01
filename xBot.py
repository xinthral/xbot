from apiHandler import API
from ircHandler import IRC
from utils import cnf

class NerdKommander:

    def __init__(self):
        self.channels = [channel.strip() for channel in cnf('SERVER', 'CHANNELS').lower().split(',')]
        print(self.channels)
        self.irc = IRC(self.channels)
        self.irc.run()

if __name__ == '__main__':
    bot = NerdKommander()
