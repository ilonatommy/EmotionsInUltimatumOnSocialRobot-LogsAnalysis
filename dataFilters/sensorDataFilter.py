from models.emotionModel import EmotionModel
from enums.emotionSourceEnum import EmotionSourceEnum
from config import Config

import numpy as np
import warnings


class SensorDataFilter:
    def __init__(self):
        self.audio_ratio = Config().audio_ratio
        self.video_ratio = 1.0 - Config().audio_ratio

    def __try_mean_probs(self, probs):
        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                mean_probs = np.mean(probs, 0)
                return mean_probs
            except RuntimeWarning:
                return np.zeros(7)

    def filter_stage_emotions(self, stage):
        probs_v = stage.get_video_emotions_probabilities()
        probs_a = stage.get_audio_emotions_probabilities()
        mean_probs_v = self.__try_mean_probs(probs_v)
        mean_probs_a = self.__try_mean_probs(probs_a)
        filtered_emos = mean_probs_v * self.video_ratio + mean_probs_a * \
        self.audio_ratio
        max_class = np.argmax(filtered_emos)
        return EmotionModel(stage.start_time, \
        EmotionSourceEnum.FILTERED_SENSORS, \
        "", max_class, \
        filtered_emos, Config().emotion_labels[max_class])
