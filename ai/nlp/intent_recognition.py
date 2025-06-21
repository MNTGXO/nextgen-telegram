from typing import Dict, Any
import numpy as np
import onnxruntime as ort

class IntentRecognizer:
    def __init__(self, model_path: str):
        self.session = ort.InferenceSession(model_path)
        self.labels = ["command", "question", "spam", "normal"]
        
    async def predict(self, text: str) -> Dict[str, float]:
        inputs = self._preprocess(text)
        outputs = self.session.run(None, inputs)
        probs = self._softmax(outputs[0][0])
        return {label: float(prob) for label, prob in zip(self.labels, probs)}
    
    def _preprocess(self, text: str) -> Dict[str, Any]:
        # Simplified text processing
        tokens = text.lower().split()
        return {"input": np.array([tokens], dtype=np.int64)}
    
    def _softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()
