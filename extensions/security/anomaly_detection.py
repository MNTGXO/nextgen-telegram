from datetime import datetime, timedelta
from collections import defaultdict

class AnomalyDetector:
    def __init__(self, threshold: int = 10, window: int = 60):
        self.threshold = threshold
        self.window = window  # seconds
        self.activity_log = defaultdict(list)
        
    def check_activity(self, user_id: int) -> bool:
        now = datetime.now()
        # Clean old records
        self.activity_log[user_id] = [
            t for t in self.activity_log[user_id]
            if now - t < timedelta(seconds=self.window)
        ]
        # Check if activity exceeds threshold
        if len(self.activity_log[user_id]) >= self.threshold:
            return False
        self.activity_log[user_id].append(now)
        return True
