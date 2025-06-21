# Advanced Usage Guide

## AI Integration
```python
from nextgen_telegram.ai.nlp import IntentRecognizer

recognizer = IntentRecognizer("models/intent.onnx")
intent = await recognizer.predict("How do I reset my password?")
```

## Blockchain Audit Trail
```python
audit = BlockchainAudit()
tx_hash = await audit.log_operation(
    "user_login",
    {"user_id": 123, "ip": "192.168.1.1"}
)
```

## Media Processing Pipeline
```python
from nextgen_telegram.extensions.media import MediaProcessor

processor = MediaProcessor()
await processor.process("input.jpg", "output.jpg", "image")
```
