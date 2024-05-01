from utils.libs import *
from utils.varables import *

def get_friends(self):
    url = "https://discord.com/api/users/@me/relationships"
    r = self.session.get(url)
    return r.json() if r.status_code == 200 else []