from utils.libs import *
from utils.Functions.Get_Messages import *
from utils.varables import *

def clear_messages(self, channel_id: str) -> None:
    """It will delete messages from a channel"""
    total_messages_url = f"https://discord.com/api/channels/{channel_id}/messages/search?author_id={self.id}"
    total_messages = requests.get(total_messages_url, headers=self.HEADERS).json()["total_results"]
    page = 0
    total = 0
    while total <= total_messages:
        messages = self.get_messages(channel_id, page)
        for message in messages:
            if message[0]["author"]["id"] == self.id:
                url = f"https://discord.com/api/channels/{channel_id}/messages/{message[0]['id']}"
                r = requests.delete(url, headers=self.HEADERS)
                print(r.status_code, r.text)
                if r.status_code in [200, 201, 204]:
                    print(CGREEN + f"{self.username} | Deleted message {message[0]['id']}", {CRESET})
                    time.sleep(2)
                    total += 1
                else:
                    print(r.status_code)
                    print(r.text)
        page += 1
    print(CRESET + f"{MESSAGE_OK} {CGREEN}Deleted Messages {CYELLOW}{total} {CGREEN}In {CYELLOW}{channel_id} {CYELLOW}To User: {CBLUE}{self.username}" + CRESET)