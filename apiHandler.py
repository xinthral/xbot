import json
import requests
from utils import cnf
from pprint import pprint as pp

# Turn keepalive off for session connections
# Default is True
#s = requests.session()
#s.config['keep_alive'] = False

client_id = cnf('AUTH', 'CLIENT_ID')
APIURL = 'https://api.twitch.tv/helix/'
HEADERS = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.helix+json'}
DEBUG = cnf('DEV', 'DEBUG')

def api_streams(args=None):
    """ Pulls Streams API from Twitch """
    method = 'streams'
    if args != None:
        method = method + '?'
        count = len(args.items())
        for k,v in args.items():
            method += "{}={}".format(k, v)
            count -= 1
            if count > 0:
                method += '&'
    response = requests.get(APIURL + method, headers=HEADERS).json()
    if DEBUG:
        pp(response)
    return(response)

def api_users(args=None):
    """ Pulls Users API from Twitch """
    method = 'users'
    if args != None:
        method = method + '?'
        count = len(args.items())
        for k,v in args.items():
            method += "{}={}".format(k, v)
            count -= 1
            if count > 0:
                method += '&'
    response = requests.get(APIURL + method, headers=HEADERS).json()
    if DEBUG:
        pp(response)
    return(response)

def api_games(args=None):
    """ Pulls Games API from Twitch """
    method = 'games'
    if args != None:
        method = method + '?'
        count = len(args.items())
        for k,v in args.items():
            method += "{}={}".format(k, v)
            count -= 1
            if count > 0:
                method += '&'
    response = requests.get(APIURL + method, headers=HEADERS).json()
    if DEBUG:
        pp(response)
    return(response)

def tmi_chatters(args=None):
    """ Pulls Chatter stats from Twitch """
    if args != None:
        url = "https://tmi.twitch.tv/group/user/{}/chatters".format(args)
        response = requests.get(url).json()
        if DEBUG:
            pp(response)
        return(response)
    else:
        pass

def api_follows(args=None):
    """ Pulls Follower API from Twitch """
    method = 'follows'
    if args != None:
        method = method + '?'
        count = len(args.items())
        for k,v in args.items():
            method += "{}={}".format(k, v)
            count -= 1
            if count > 0:
                method += '&'
    response = requests.get(APIURL + method, headers=HEADERS).json()
    if DEBUG:
        pp(response)
    return(response)

def api_channel(args=None):
    """ Polls Channels Method from Twitch """
    if args != None:
        url = "https://api.twitch.tv/kraken/channels/{}/videos".format(args)
        response = requests.get(url).json()
        if DEBUG:
            pp(response)
        return(response)
    else:
        pass
