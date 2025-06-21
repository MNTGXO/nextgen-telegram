class SmartReplyEngine:
    def __init__(self, model_path=None):
        self.model = self._load_model(model_path) or self._download_default()
        self.context_window = 5  # Last 5 messages as context
        
    async def generate_reply(self, message_history):
        context = self._prepare_context(message_history)
        reply = await self._call_model(context)
        return self._post_process(reply)
    
    async def _call_model(self, context):
        # Implementation using ONNX runtime for performance
        inputs = self.tokenizer(context, return_tensors="np")
        outputs = await self.model.run(None, inputs)
        return self.tokenizer.decode(outputs[0])
