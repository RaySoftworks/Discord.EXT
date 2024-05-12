from utils.libs import *
from utils.varables import *
from utils.Functions.Get_Gifts_Status import *
from utils.Functions.Get_Nitro_Status import *
from utils.Functions.Get_Payments_Status import *



def dump_info(self, extra_info: bool = False):
    info = {
        "token": self.token,
        "username": self.username,
        "id": self.id,
        "email": self.email,
        "phone": self.phone,
        "nitro": self.get_nitro(),
        "gifts": self.get_gifts(),
        "payments": self.get_payments()
    }

    count = 1
    while os.path.isfile(f"Dumped Info To User {self.username}{count}.json"):
        count += 1

    filename = f"Dump_User.{self.username}{count}.json"
    path = os.path.abspath(filename)
    print(f"{MESSAGE_OK} {CGREEN}Info Dumped{CRESET}: {CBLUE}{self.username}" + CRESET)
    print(f"{MESSAGE_INDIFFERENCE} {CGREEN}Dump Path{CRESET}: {CBLUE}{path}" + CRESET)

    if extra_info:
        info["friends"] = self.get_friends(),
        info["user_dm"] = self.get_user_channels(),
        info["guilds"] = self.get_guilds()

    with open(f"Dump_User.{self.username}{count}.json", "w") as f:
        json.dump(info, f, indent=4)
