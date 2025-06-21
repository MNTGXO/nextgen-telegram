import asyncio
from typing import Optional

class MTProtoTCPTransport:
    def __init__(self, host: str = "149.154.167.50", port: int = 443):
        self.host = host
        self.port = port
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        
    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(
            self.host, self.port, ssl=True
        )
        
    async def send(self, data: bytes):
        if not self.writer:
            await self.connect()
        self.writer.write(data)
        await self.writer.drain()
        
    async def receive(self) -> bytes:
        if not self.reader:
            await self.connect()
        return await self.reader.read(4096)
