from utils.libs import *
from utils.varables import *

def get_guilds(self) -> list:
    """It will get all the servers of the account"""
    url = "https://discord.com/api/users/@me/guilds"
    r = requests.get(url, headers=self.HEADERS)
    return r.json() if r.status_code == 200 else []