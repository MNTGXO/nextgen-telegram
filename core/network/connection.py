import asyncio
import aiohttp
from typing import Optional

class BaseConnection:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def connect(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout)
        )
        
    async def close(self):
        if self.session:
            await self.session.close()
            
    async def request(self, method: str, url: str, **kwargs):
        if not self.session:
            await self.connect()
        async with self.session.request(method, url, **kwargs) as resp:
            return await resp.json()
