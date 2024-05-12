#Imports
import os
import time

from utils.libs import *
from utils.varables import *

#CheckLibs
os.system("cls")
os.system("pip install -r requirements.txt")
time.sleep(1.5)
os.system("cls")

#LaunchMessage
print(f"{CRESET}{MESSAGE_OK} {CGREEN}Succesfully Launched{CRESET}")
time.sleep(0.5)

#TokenShowPrompt
ShowToken = input(USER_INPUT + f"{CCYAN}Show Token Y/N:{CYELLOW}")
os.system("cls")

class EXT:
    #ImportFunctions
    from utils.Functions.Get_User_Channels import get_user_channels
    from utils.Functions.Set_Custom_Status import set_custom_status
    from utils.Functions.Get_Payments_Status import get_payments
    from utils.Functions.Delete_Channels import delete_channels
    from utils.Functions.Clear_Messages import clear_messages
    from utils.Functions.Delete_Friends import delete_friends
    from utils.Functions.Change_Status import change_status
    from utils.Functions.Delete_Guilds import delete_guilds
    from utils.Functions.Get_Gifts_Status import get_gifts
    from utils.Functions.Get_Nitro_Status import get_nitro
    from utils.Functions.Get_Messages import get_messages
    from utils.Functions.Get_Friends import get_friends
    from utils.Functions.Get_Guilds import get_guilds
    from utils.Functions.Quick_Mode import QuickMode
    from utils.Functions.Dump_Info import dump_info
    from utils.Functions.Set_Bio import set_bio

    def __init__(self, token):
        self.token = token
        self.session = Session()
        self.session.headers = {"authorization": self.token, "content-type": "application/json"}

        self.api = "https://discord.com/api"
        self.token = token
        self.username = None
        self.id = None
        self.email = None
        self.phone = None
        self.api = None

        self.HEADERS = {"authorization": self.token, "content-type": "application/json"}
        self.TokenValidate()

    #CheckToken
    def TokenValidate(self):
        url = f"https://discord.com/api/users/@me"
        r = self.session.get(url)
        if r.status_code == 200:
            if ShowToken.lower() in ShowTokenTrue:
                print(MESSAGE_OK + CGREEN + f" Valid token: {self.token}" + CRESET)
                time.sleep(2)
            else:
                None
            data = r.json()
            self.username = data['username']
            self.id = data['id']
            self.email = data['email']
            self.phone = data['phone']
        else:
            print(f"{CRESET} {MESSAGE_ERROR}{CRED}Invalid Token{CRESET}")
            exit()

CRESET

#EnterTokenPrompt
if ShowToken.lower() in ShowTokenTrue:
    TokenShow = True
    user = EXT(token=input(f"{CRESET}{USER_INPUT}{CCYAN}Enter Discord Token{CRESET}:{CYELLOW}{CRESET}"))
    time.sleep(0.5)
    os.system(f"cls")
else:
    TokenShow = False
    userx = EXT(token=getpass(f"{CRESET}{USER_INPUT}{CCYAN}Enter Discord Token{CRESET}:{CYELLOW}"))
    time.sleep(0.5)
    os.system(f"cls")

#MainProgramStart
while MenuEnable == True:
    #MenuBegin
    print(Baner)
    UCC = input(f"{CRESET}{USER_INPUT}")

    if TokenShow == True:
        #QuickMode
        if UCC == "1":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} QuickMode Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            user.QuickMode()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #MessageDelete
        if UCC == "2":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Messages Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            user.clear_messages(channel_id=input(f"{CRESET}{USER_INPUT}{CCYAN}Input Channel ID{CRESET}:{CYELLOW}"))
            time.sleep(2)
            input(MESSAGE_SUCCESS)
            os.system("cls")
        #DeleteGuilds
        if UCC == "3":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Guilds Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            user.delete_guilds()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #DeleteChannels
        if UCC == "4":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Channels Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            user.delete_channels()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #DeleteFriends
        if UCC == "5":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Friends Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            user.delete_friends()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #SetNewBio
        if UCC == "6":
            user.set_bio(bio="New Bio")
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #SetCustomStatus
        if UCC == "7":
            user.set_custom_status(status=input(f"{USER_INPUT}"))
            time.sleep(2)
            input(MESSAGE_SUCCESS)
            os.system("cls")
        #ChangeUserStatus
        if UCC == "8":
            user.change_status(status=input(
                f'{USER_INPUT} {CRESET}["{CCYAN}online{CRESET}", "{CCYAN}idle{CRESET}", "{CCYAN}dnd{CRESET}", "{CCYAN}invisible{CRESET}"]{CRESET}: '))
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        if UCC == "9":
            user.dump_info()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #ExitOptions
        if UCC.lower() in ExitOptions:
            os.system("cls")
            MenuEnable = False
        else:
            os.system("cls")

    if TokenShow == False:
        #QuickMode
        if UCC == "1":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} QuickMode Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            userx.QuickMode()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #MessageDelete
        if UCC == "2":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Messages Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            userx.clear_messages(channel_id=input(f"{CRESET}{USER_INPUT}{CCYAN}Input Channel ID:{CYELLOW}"))
            time.sleep(2)
            input(MESSAGE_SUCCESS)
            os.system("cls")
        #DeleteGuilds
        if UCC == "3":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Guilds Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            userx.delete_guilds()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #DeleteChannels
        if UCC == "4":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Channels Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            userx.delete_channels()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #DeleteFriends
        if UCC == "5":
            input(f"{CRESET}{MESSAGE_INDIFFERENCE} Delete Friends Warning (Press Any Key... <2.5s>)")
            time.sleep(2.5)
            userx.delete_friends()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #SetNewBio
        if UCC == "6":
            userx.set_bio(bio="New Bio")
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #SetCustomStatus
        if UCC == "7":
            userx.set_custom_status(status=input(f"{USER_INPUT}"))
            time.sleep(2)
            input(MESSAGE_SUCCESS)
            os.system("cls")
        #ChangeUserStatus
        if UCC == "8":
            userx.change_status(status=input(
                f'{USER_INPUT} {CRESET}["{CCYAN}online{CRESET}", "{CCYAN}idle{CRESET}", "{CCYAN}dnd{CRESET}", "{CCYAN}invisible{CRESET}"]{CRESET}: '))
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        if UCC == "9":
            userx.dump_info()
            input(MESSAGE_SUCCESS)
            time.sleep(2)
            os.system("cls")
        #ExitOptions
        if UCC.lower() in ExitOptions:
            os.system("cls")
            MenuEnable = False
        else:
            os.system("cls")