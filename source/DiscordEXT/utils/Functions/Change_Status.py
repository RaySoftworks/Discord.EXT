from utils.libs import *
from utils.varables import *

def change_status(self, status: str) -> None:
    """With this function you will be able to change your status"""
    url = "https://discord.com/api/v9/users/@me/settings"
    statuses = ["online", "idle", "dnd", "invisible"]
    if status in statuses:
        payload = {"status": status}
        r = requests.patch(url, headers=self.HEADERS, json=payload)
        if r.status_code in [200, 201, 204]:
            print(c_res + f"{m_a} {self.username}Changed" + c_res)
        else:
            print(CRED + f"{self.username} | Error: {r.text}" + c_res)
    else:
        print(f"{msg_error}Invalid status: {CGREEN}{statuses}" + c_res)

