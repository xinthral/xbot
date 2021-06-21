import socket
import ssl
import sys
import threading
import traceback

from msgHandler import Message
from time import sleep
from utils import cnf, LogParam

class IRC(threading.Thread):
    __delim = cnf('ADMIN', 'DELIM')
    __debug = cnf('DEV', 'DEBUG')

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
        """ Main Event loop """
        idleTimeout = 0
        while (cycle and idleTimeout < 60):
            try:
                received_msgs = self.irc.recv(1024).decode('utf-8')
                for received_msg in received_msgs.split("\r\n"):
                    if len(received_msg) > 1:
                        if IRC.__debug:
                            print(f"> {received_msg}")
                        self.parse_message(received_msg)
                        idleTimeout = 0
                    else:
                        sleep(1)
            except socket.timeout:
                # FIXME: replace with logging
                idleTimeout += 1
            except socket.gaierror:
                print(f"IRC Socket Error: {socket.gaierror}")
                cycle = False
            except KeyboardInterrupt:
                cycle = False
            except Exception as e:
                etype, etext, etrace = sys.exc_info()
                traceback.print_exception(*sys.exc_info())
                # print(f"IRC Exception Error: T: {etype}, X: {etext}, N: {etrace}")
                cycle = False

    def join_channel(self, channel):
        """ Join bot to listen in channel """
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
        """ Join multiple channels """
        for channel in channels:
            self.join_channel(channel)
            # self.send_private(channel, 'Salue senior')

    @LogParam
    def parse_message(self, message):
        """ Parse incoming messages into data object """
        if len(message) > 0:
            obj = Message.parse_message(message)
            # if obj.keys() >= {'response', 'channel'}:
            #     for row in obj['response']:
            #         if len(row.split(' ')) > 1:
            #             for resp in row:
            #                 self.send_private(obj['channel'], resp)
            #                 sleep(2)
            #         else:
            #             self.send_private(obj['channel'], row)

    def part_channel(self, channel):
        """ Remove channel from listening events """
        self.__channels.discard(channel)
        self.send_command('PART', f"#{channel}")

    def part_channels(self, channels=[]):
        """ Remove multiple channels from listening events """
        for channel in channels:
            self.part_channel(channel)

    def send_private(self, channel, text):
        """ Send socket message to specific channel """
        self.send_command('PRIVMSG', f"#{channel} :{text}")

    def send_command(self, command, text):
        """ Send socket message to with prefix irc commands """
        self.send(f"{command} {text}")

    def reconnect(self, accept=True):
        """ Reinstantiate the socket connection """
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
