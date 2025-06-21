class BlockchainAudit:
    def __init__(self, network='polygon'):
        self.web3 = Web3(Web3.HTTPProvider(self._get_rpc_url(network)))
        self.contract = self._load_contract()
        
    async def log_operation(self, operation_type, metadata):
        tx_hash = await self._send_transaction(operation_type, metadata)
        return tx_hash
    
    async def verify_operation(self, tx_hash):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        return self._validate_receipt(receipt)
