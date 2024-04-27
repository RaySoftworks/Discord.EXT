from utils.libs import *
from utils.varables import *

print(f"{c_res} {m_a} {CGREEN}Succesfully Launched{c_res}")
time.sleep(0.5)

class EXT:
    from utils.Functions.Set_Custom_Status import set_custom_status
    from utils.Functions.Delete_Channels import delete_channels
    from utils.Functions.Clear_Messages import clear_messages
    from utils.Functions.Delete_Friends import delete_friends
    from utils.Functions.Change_Status import change_status
    from utils.Functions.Delete_Guilds import delete_guilds
    from utils.Functions.Quick_Mode import QuickMode
    from utils.Functions.Set_Bio import set_bio

    def _validate(self) -> None:
        """This will check if the discord token works"""
        url = f"https://discord.com/api/users/@me"
        r = requests.get(url, headers=self.HEADERS)
        if r.status_code == 200:
            print(CGREEN + f"Valid token: {self.token}" + c_res)
            data = r.json()
            self.username = data['username'] + "#" + data['discriminator']
            self.id = data['id']
            self.email = data['email']
            self.phone = data['phone']
        else:
            print(f"{c_res} {msg_error}{CRED}Invalid Token{c_res}")
            exit()

    def __init__(self, token):
        self.token = token

        self.username = None
        self.id = None
        self.email = None
        self.phone = None

        self.HEADERS = {"authorization": self.token, "content-type": "application/json"}
        self._validate()


user = EXT(token=getpass(f"{c_res} {U_in}Token: {c_cyan}"))
time.sleep(0.5)
os.system("cls")

quit = False

while quit == False:
    print(c_cyan + Baner)
    UCC = input(f"{c_res}{U_in}")

    if UCC == "1":
        input(f"{c_res}{m_b} QuickMode Warning (Press Any Key... <2.5s>)")
        time.sleep(2.5)
        user.QuickMode()
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
        time.sleep(2)
    if UCC == "2":
        input(f"{c_res}{m_b} Delete Messages Warning (Press Any Key... <2.5s>)")
        time.sleep(2.5)
        user.clear_messages(channel_id=input(f"{c_res}{U_in}Input Channel ID: "))
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "3":
        input(f"{c_res}{m_b} Delete Guilds Warning (Press Any Key... <2.5s>)")
        time.sleep(2.5)
        user.delete_guilds()
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "4":
        input(f"{c_res}{m_b} Delete Channels Warning (Press Any Key... <2.5s>)")
        time.sleep(2.5)
        user.delete_channels()
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "5":
        input(f"{c_res}{m_b} Delete Friends Warning (Press Any Key... <2.5s>)")
        time.sleep(2.5)
        user.delete_friends()
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "6":
        user.set_bio(bio="New Bio")
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "7":
        user.set_custom_status(status=input(f"{U_in}"))
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "8":
        user.change_status(status=input(
            f"{U_in} {c_res}['{c_cyan}online{c_res}', '{c_cyan}idle{c_res}', '{c_cyan}dnd{c_res}', '{c_cyan}invisible{c_res}']{c_res}: "))
        print(f"{c_res}{m_a} Success (Click Anything To Continue)")
        os.system("cls")
    if UCC == "0":
        os.system("cls")
        exit()
    else:
        os.system("cls")