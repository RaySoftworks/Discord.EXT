from utils.libs import *
from utils.varables import *

def delete_guilds(self, exceptions: list = []) -> None:
    """It will delete all the servers from the account"""
    total = 0
    for guild in self.get_guilds():
        if guild["id"] in exceptions:
            continue
        if guild['owner']:
            url = f"https://discord.com/api/guilds/{guild['id']}/delete"
            r = requests.post(url, headers=self.HEADERS, json={})
            if r.status_code in [200, 201, 204]:
                total += 1
        else:
            url = f"https://discord.com/api/users/@me/guilds/{guild['id']}"
            requests.delete(url, headers=self.HEADERS, json={})
    print(CRESET + f"{MESSAGE_OK} {CGREEN}Deleted {CYELLOW}{total} {CGREEN}Guilds To User: {CBLUE}{self.username}" + CRESET)