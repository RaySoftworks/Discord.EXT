from utils.libs import *

#Colors
CGREEN = colorama.Fore.GREEN
CRED = colorama.Fore.RED
CYELLOW = colorama.Fore.YELLOW
CCYAN = colorama.Fore.CYAN
CBLUE = colorama.Fore.BLUE
CRESET = colorama.Fore.RESET

VERSION = f"{CYELLOW}2.1{CRESET}"

#Messages
MESSAGE_OK = (CRESET + "(" + CCYAN + "+" + CRESET + ")" + CRESET)
USER_INPUT = (CRESET + "(" + CCYAN + ">" + CRESET + ") " + CYELLOW)
MESSAGE_INDIFFERENCE = (CRESET + "(" + CBLUE + "~" + CRESET + ")" + CRESET)
MESSAGE_SUCCESS = (f"{CRESET}{MESSAGE_OK}{CGREEN} Success {CBLUE}({CRED}Press Any Key... {CCYAN}<{CRESET}2{CYELLOW}.{CRESET}0s{CCYAN}>{CBLUE}){CRESET}")

#Error Messages
MESSAGE_BAD = (CRESET + "(" + CRED + "-" + CRESET + ")" + CRESET)
MESSAGE_ERROR = (MESSAGE_BAD + CRED + " Something Went Wrong" + CRESET + " > ")

#Options
TokenShow = None
ShowTokenTrue = ["y", "Y", "Yes", "YES"]
ExitOptions = ["0", "Exit", "exit", "Exot", "exot", "Expt", "expt"]

#MenuSettings
MenuEnable = True

#Baner
Baner = f"""
{VERSION}
{CCYAN}
_____________________________________________________  _____________  _________
___  __ \___  _/_  ___/_  ____/_  __ \__  __ \__  __ \ ___  ____/_  |/ /__  __/
__  / / /__  / _____ \_  /    _  / / /_  /_/ /_  / / / __  __/  __    /__  /   
_  /_/ /__/ /  ____/ // /___  / /_/ /_  _, _/_  /_/ /___  /___  _    | _  /    
/_____/ /___/  /____/ \____/  \____/ /_/ |_| /_____/_{CYELLOW}(_){CCYAN}_____/  /_/|_| /_/       
{CCYAN}─────────────────────────────────────────────────────────────────────────{CRESET}
{CCYAN}[{CYELLOW}1{CCYAN}] Quick Mode
{CCYAN}[{CYELLOW}2{CCYAN}] Delete Messages
{CCYAN}[{CYELLOW}3{CCYAN}] Delete Guilds
{CCYAN}[{CYELLOW}4{CCYAN}] Delete Channels
{CCYAN}[{CYELLOW}5{CCYAN}] Delete Friends       
{CCYAN}[{CYELLOW}6{CCYAN}] Set Bio
{CCYAN}[{CYELLOW}7{CCYAN}] Set Status
{CCYAN}[{CYELLOW}8{CCYAN}] Set Own Status
{CCYAN}[{CRED}0{CCYAN}] {CCYAN}EXIT
{CCYAN}─────────────────────────────────────────────────────────────────────────{CRESET}
         
"""