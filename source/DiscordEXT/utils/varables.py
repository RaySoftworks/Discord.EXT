from utils.libs import *

CGREEN = colorama.Fore.GREEN
CRED = colorama.Fore.RED
c_cyan = colorama.Fore.CYAN
c_blue = colorama.Fore.BLUE
c_res = colorama.Fore.RESET
VERSION = '2.0.0'

m_a = (c_res + "(" + c_cyan + "+" + c_res + ")" + c_res)
m_b = (c_res + "(" + c_blue + "~" + c_res + ")" + c_res)
m_c = (c_res + "(" + CRED + "-" + c_res + ")" + c_res)
U_in = (c_res + "(" + c_cyan + ">" + c_res + ") " + c_cyan)
msg_error = (m_c + CRED + " Something Went Wrong" + c_res + " >>> ")

Baner = f"""
{c_cyan}
{VERSION}
_____________________________________________________  _____________  _________
___  __ \___  _/_  ___/_  ____/_  __ \__  __ \__  __ \ ___  ____/_  |/ /__  __/
__  / / /__  / _____ \_  /    _  / / /_  /_/ /_  / / / __  __/  __    /__  /   
_  /_/ /__/ /  ____/ // /___  / /_/ /_  _, _/_  /_/ /___  /___  _    | _  /    
/_____/ /___/  /____/ \____/  \____/ /_/ |_| /_____/_(_)_____/  /_/|_| /_/       
{c_cyan}─────────────────────────────────────────────────────────────────────────{c_res}
{c_cyan}[1] Quick Mode
{c_cyan}[2] Delete Messages
{c_cyan}[3] Delete Guilds
{c_cyan}[4] Delete Channels
{c_cyan}[5] Delete Friends       
{c_cyan}[6] Set Bio
{c_cyan}[7] Set Status
{c_cyan}[8] Set Own Status
{c_cyan}[{CRED}0{c_cyan}] {CRED}EXIT
{c_cyan}─────────────────────────────────────────────────────────────────────────{c_res}         
{c_res}
"""