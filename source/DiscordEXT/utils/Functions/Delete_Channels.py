from utils.libs import *
from utils.varables import *

def delete_channels(self) -> None:
    """It will delete all the channels from the account"""
    total = 0
    for channel in self.get_user_channels():
        url = f"https://discord.com/api/channels/{channel['id']}"
        r = requests.delete(url, headers=self.HEADERS)
        if r.status_code in [200, 201, 204]:
            total += 1
    print(f"{self.username} | Deleted {total} channels")
