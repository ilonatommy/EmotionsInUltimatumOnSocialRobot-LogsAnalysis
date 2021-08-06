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

    def filter_stage_emotions(self, stage, get_stage_video_probabilities_fun, \
        get_stage_audio_probabilities_fun):
        probs_v = get_stage_video_probabilities_fun()
        probs_a = get_stage_audio_probabilities_fun()
        if len(probs_v.shape) == len(probs_a.shape):
            probs = np.append(probs_v, probs_a, 0)
        else:
            if len(probs_v.shape) == 1:
                probs = probs_a
            else:
                probs = probs_v
        filtered_emos = self.__try_mean_probs(probs)
        max_class = np.argmax(filtered_emos)
        return EmotionModel(stage.start_time, \
        EmotionSourceEnum.FILTERED_SENSORS, \
        "", max_class, \
        filtered_emos, Config().emotion_labels[max_class])
