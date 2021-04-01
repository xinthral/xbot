import json
import requests
from utils import cnf

class API:
    # Get the channel id, we will need this for new API calls
    _helix_url = 'https://api.twitch.tv/helix/'

    def getAppSessionToken():
        pass

    def __init__(self, bot_id):
        self.__bid = bot_id
        self.__ses = ''


class CLIENT:
    def __init__(self, client_id, client_secret):
        self.__cid = client_id
        self.__sec = client_secret

    def setup(self):
        self.headers = {
            'Client-ID': self.client_id,
            'Authorization': f'OAuth {self.__ses}',
            'Accept': 'application/vnd.twitchtv.helix+json',
            }
class TMI:
    pass
