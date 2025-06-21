from nextgen_telegram import AsyncTelegramClient
from extensions.blockchain import BlockchainAudit

class EnterpriseBot(AsyncTelegramClient):
    def __init__(self, session_name, api_id, api_hash):
        super().__init__(session_name, api_id, api_hash)
        self.audit = BlockchainAudit(network='polygon')
        
    async def send_audited_message(self, chat_id, text):
        tx_hash = await self.audit.log_operation(
            "send_message",
            {"chat_id": chat_id, "text": text}
        )
        result = await self.send_message(chat_id, text)
        await self.audit.log_operation(
            "message_sent",
            {"message_id": result.message_id, "tx_hash": tx_hash}
        )
        return result
