class ProtocolRouter:
    def __init__(self, config):
        self.protocols = {
            'mtproto': MProtoHandler(config),
            'botapi': BotAPIHandler(config),
            'tdlib': TDLibHandler(config)
        }
        self.strategy = config.get('routing_strategy', 'auto')
        
    async def route_request(self, method, params):
        if self.strategy == 'auto':
            return await self._auto_route(method, params)
        else:
            return await self.protocols[self.strategy].execute(method, params)
    
    async def _auto_route(self, method, params):
        # AI-based protocol selection
        latency = await self._measure_latency()
        if method in ['sendMessage', 'getUpdates'] and latency < 200:
            return await self.protocols['botapi'].execute(method, params)
        else:
            return await self.protocols['mtproto'].execute(method, params)
