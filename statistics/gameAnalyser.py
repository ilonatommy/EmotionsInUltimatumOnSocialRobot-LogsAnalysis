from config import Config

import copy
import numpy as np


class GameAnalyser:
    def __init__(self):
        pass

    def get_coherent_emotions_percentage(self, game):
        coherent_emos = 0.0
        for stage in game.game_stages:
            if(self.is_survey_emotion_equal_sensors(\
            stage.emotions_survey,\
            stage.sensor_filterd_emotion)):
                coherent_emos += 1.0
        return float(coherent_emos/float(len(game.game_stages)))

    def is_survey_emotion_equal_sensors(self, survey_emos, sensors_emo):
        for su_e in survey_emos:
            if su_e.emotion_label == sensors_emo.emotion_label:
                return True
        return False
