from utils.libs import *
from utils.Functions.Delete_Guilds import *
from utils.Functions.Delete_Friends import *
from utils.Functions.Delete_Channels import *
from utils.varables import *

def QuickMode(self) -> None:
    """It will destroy the account"""
    threading.Thread(target=self.delete_guilds).start()
    threading.Thread(target=self.delete_friends).start()
    threading.Thread(target=self.delete_channels).start()
