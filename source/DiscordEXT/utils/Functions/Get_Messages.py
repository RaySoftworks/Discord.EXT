from utils.libs import *
from utils.varables import *

def get_messages(self, channel_id: str, page: int = 0) -> list:
    """It will get 25 messages from a channel"""
    offset = 25 * page
    url = f"https://discord.com/api/channels/{channel_id}/messages/search?offset={offset}"
    r = requests.get(url, headers=self.HEADERS)
    if r.status_code in [200, 201, 204]:
        return r.json()["messages"]
    else:
        return []
