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
