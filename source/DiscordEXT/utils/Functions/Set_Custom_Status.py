from utils.libs import *
from utils.varables import *

def set_custom_status(self, status: str) -> None:
    """It will set a new custom status"""
    url = "https://discord.com/api/users/@me/settings"
    status = {"custom_status": {"text": status}}
    r = requests.patch(url, headers=self.HEADERS, json=status)
    if r.status_code in [200, 201, 204]:
        print(c_res + f"{m_a} {self.username}Changed" + c_res)
    else:
        print(f"{msg_error}{self.username}{CRED} {r.text}" + c_res)
