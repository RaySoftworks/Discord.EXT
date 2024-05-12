from utils.libs import *
from utils.varables import *


def get_gifts(self):
    url = f"https://discord.com/api/users/@me/entitlements/gifts"
    r = requests.get(url, headers=self.HEADERS)
    return r.json() if r.status_code == 200 else []