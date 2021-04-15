import json
import requests
from utils import cnf

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
