from utils.libs import *
from utils.varables import *

def get_user_channels(self) -> list:
    """It will get all the dm of the account"""
    url = f"https://discordapp.com/api/users/@me/channels"
    r = requests.get(url, headers=self.HEADERS)
    return r.json() if r.status_code == 200 else []