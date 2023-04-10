from highrise import BaseBot, User, SessionMetadata
from highrise.models import SessionMetadata, User, Item, Position
import random

class Bot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to(Position(7.5,0.4,1.5,"FrontLeft"))

        pass

    username_to_id = {}
    async def on_user_join(self, user: User) -> None:
        print(f"[JOIN   ] {user.username}")
        self.username_to_id[user.username] = user.id
        await self.highrise.chat(f"welcome to HOME, @{user.username}!")
        
    async def on_chat(self, user: User, message: str) -> None:  
        if message.startswith("/give up"):
            await self.highrise.send_emote("emoji-give-up", user.id)
