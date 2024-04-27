from utils.libs import *
from utils.varables import *

def delete_friends(self) -> None:
    """It will delete all the friends from the account"""
    total = 0
    for friend in self.get_friends():
        url = f"https://discord.com/api/users/@me/relationships/{friend['id']}"
        r = requests.delete(url, headers=self.HEADERS)
        if r.status_code in [200, 201, 204]:
            total += 1
    print(f"{self.username} | Deleted {total} friends")