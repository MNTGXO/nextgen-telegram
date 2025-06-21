from typing import Optional
from core.network import ProtocolRouter
from core.session import SessionManager

class AsyncTelegramClient:
    def __init__(self, session_name: str, api_id: Optional[int] = None, api_hash: Optional[str] = None):
        self.session = SessionManager(session_name)
        self.router = ProtocolRouter({
            'api_id': api_id,
            'api_hash': api_hash
        })
        
    async def start(self):
        session_data = await self.session.load_session()
        if session_data:
            await self.router.initialize(session_data)
        else:
            await self._perform_first_time_auth()
            
    async def send_message(self, chat_id: int, text: str):
        return await self.router.route_request(
            "sendMessage",
            {"chat_id": chat_id, "text": text}
        )
