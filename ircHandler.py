import socket
import ssl
import sys
import threading
from msgHandler import Message
from time import sleep
from utils import cnf

class IRC(threading.Thread):
    __delim = cnf('ADMIN', 'DELIM')
    def __init__(self, channels=list()):
        super().__init__()
        # self.__bot_id = cnf('AUTH', 'BOT_ID')
        # self.__bot_secret = cnf('AUTH', 'BOT_SECRET')
        self.__bot_oauth = cnf('AUTH', 'BOT_OAUTH')
        self.__nic = cnf('AUTH', 'NICK').lower()
        self.irc = None
        self.channels = channels
        self.__channels = set()

    def add_channel(self, channel):
        self.__channels.add(channel)

    def authenticate(self):
        self.send_command('PASS', f"oauth:{self.__bot_oauth}")
        self.send_command('NICK', self.__nic)

    def current_channels(self):
        return(self.__channels)

    def connect(self):
        server = 'irc.chat.twitch.tv'
        port = 6697
        self.irc = ssl.wrap_socket(socket.socket())
        self.irc.settimeout(1)
        # FIXME: replace with logging
        print(f"Connecting to {server} on port {port}...")
        self.irc.connect((server, port))

    def __loop(self, cycle=True):
        idleTimeout = 0
        while (cycle and idleTimeout < 60):
            try:
                received_msgs = self.irc.recv(1024).decode('utf-8')
                for received_msg in received_msgs.split("\r\n"):
                    if len(received_msg) > 1:
                        self.parse_message(received_msg)
                        idleTimeout = 0
                    # else:
                    #     sleep(3)
            except socket.timeout:
                # FIXME: replace with logging
                idleTimeout += 1
            except socket.gaierror:
                print(f"IRC Socket Error: {socket.gaierror}")
                cycle = False
            except Exception as e:
                print(f"IRC Exception Error: {sys.exc_info()[1]}")
                # cycle = False
            except KeyboardInterrupt:
                cycle = False

    def join_channel(self, channel):
        if channel in self.__channels:
            return
        self.__channels.add(channel)
        print(f"Joining {channel}...")
        self.send_command('CAP', 'REQ :twitch.tv/membership')
        self.send_command('CAP', 'REQ :twitch.tv/tags')
        self.send_command('CAP', 'REQ :twitch.tv/commands')
        self.send_command('JOIN', f"#{channel}")
        print(f"Joined {channel}!")

    def join_channels(self, channels=[]):
        for channel in channels:
            self.join_channel(channel)
            # self.send_private(channel, 'Salue senior')

    def parse_message(self, message=None):
        from pprint import pprint as pp
        if message != None:
            print(f"> {message}")
            obj = Message.parse_message(message)
            if len(obj.keys()) > 0 and 'response' in obj.keys():
                pp(obj)
                for row in obj['response']:
                    for resp in row:
                        self.send_private(obj['channel'], resp)
                        sleep(2)
            # obj['category'] = 'USERSTATE'
            # return(obj)

    def part_channel(self, channel):
        self.__channels.discard(channel)
        self.send_command('PART', f"#{channel}")

    def part_channels(self, channels=[]):
        for channel in channels:
            self.part_channel(channel)

    def send_private(self, channel, text):
        self.send_command('PRIVMSG', f"#{channel} :{text}")

    def send_command(self, command, text):
        self.send(f"{command} {text}")

    def reconnect(self, accept=True):
        if accept:
            print('Warning: Connection Required, connecting now...')
            self.connect()
        else:
            # RAISE EXCEPTION
            print('Error: Connection failed.')

    def run(self):
        """ Sets bot thread running """
        self.connect()
        self.authenticate()
        self.join_channels(self.channels)
        self.__loop()
        self.tear_down()

    def send(self, output):
        """ Send message through socket """
        # Exclusion to avoid outputting tokens to logs
        if output[:4] != 'PASS':
            print(f"< {output}")

        # If socket isn't empty, send message or reconnect
        if self.irc != None:
            self.irc.send(f"{output}\r\n".encode())
        else:
            self.reconnect()
            self.send(output)

    def tear_down(self):
        """ Initiate Teardown Sequence """
        print("Shutting Down...")
        self.irc.close()
        # exit()
