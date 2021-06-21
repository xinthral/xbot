from apiHandler import API
from ircHandler import IRC
from utils import cnf

class NerdKommander:
    def __init__(self, channels=list()):
        self.irc = IRC(channels)
        self.irc.run()

if __name__ == '__main__':
    import sys
    channels = ['nerdkommander']
    if len(sys.argv) < 2:
        channels.append('xinthral')
    else:
        [channels.append(arrg) for arrg in sys.argv[1:]]

    bot = NerdKommander(channels)
