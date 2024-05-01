from utils.libs import *
from utils.varables import *
from utils.Functions.Get_User_Channels import *

def delete_channels(self) -> None:
    """It will delete all the channels from the account"""
    total = 0
    for channel in self.get_user_channels():
        url = f"https://discord.com/api/channels/{channel['id']}"
        r = requests.delete(url, headers=self.HEADERS)
        if r.status_code in [200, 201, 204]:
            total += 1
    print(CRESET + f"{MESSAGE_OK} {CGREEN}Deleted Channels {CYELLOW}{total} To User: {CBLUE}{self.username}" + CRESET)
