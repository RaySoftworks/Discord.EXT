from utils.libs import *
from utils.varables import *

def set_bio(self, bio: str) -> None:
    """It will set a new bio"""
    url = "https://discord.com/api/v9/users/@me"
    payload = {"bio": bio}
    r = requests.patch(url, headers=self.HEADERS, json=payload)
    if r.status_code in [200, 201, 204]:
        print(CRESET + f"{MESSAGE_OK} {self.username}Changed" + CRESET)
    else:
        print(f"{MESSAGE_ERROR}{self.username}{CRED} {r.text}" + CRESET)
