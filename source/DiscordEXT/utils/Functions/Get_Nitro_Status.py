from utils.libs import *
from utils.varables import *


def get_nitro(self):
    url = f"https://discord.com/api/users/{self.id}/profile"
    r = requests.get(url, headers=self.HEADERS)
    try:
        return bool(r.json()["premium_since"])
    except KeyError("premium_since"):
        return False