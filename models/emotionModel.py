from enums.emotionSourceEnum import EmotionSourceEnum

from datetime import datetime


class EmotionModel:
    def __init__(self, emotion_timestamp, emotion_source, \
    data_sourcefile_path, emotion_class, probabilities, emotion_label):
        # type: (EmotionModel, datetime, EmotionSourceEnum, string, int, numpy.double, string) -> None:
        self.emotion_timestamp = emotion_timestamp
        self.emotion_source = emotion_source
        self.data_sourcefile_path = data_sourcefile_path
        self.emotion_class = emotion_class
        self.probabilities = probabilities
        self.emotion_label = emotion_label

    def __repr__(self):
        return '{emotion_label}'.format(\
        emotion_label=self.emotion_label)

    def __str__(self):
        return '{emotion_label}'.format(\
        emotion_label=self.emotion_label)

    def __eq__(self, x):
        if self.emotion_class == x.emotion_class and \
        self.emotion_label == x.emotion_label:
            return True
        return False
