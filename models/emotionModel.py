from datetime import datetime
from enums.emotionSourceEnum import EmotionSourceEnum

class EmotionModel:
    def __init__(self, emotion_timestamp, emotion_source):
        # type: (EmotionModel, datetime, EmotionSourceEnum) -> None:
        self.emotion_timestamp = emotion_timestamp
        self.emotion_source = emotion_source
