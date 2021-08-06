from config import Config

import copy
import numpy as np


class GameAnalyser:
    def __init__(self):
        pass

    def get_my_ai_vs_survey_coherent_emotions_percentage(self, game):
        coherent_emos = 0.0
        for stage in game.game_stages:
            if(self.are_emotions_equal(\
            stage.emotions_survey,\
            [stage.sensor_filterd_emotion])):
                coherent_emos += 1.0
        return float(coherent_emos/float(len(game.game_stages)))

    def get_reference_ai_vs_survey_coherent_emotions_percentage(self, game):
        coherent_emos = 0.0
        for stage in game.game_stages:
            if(self.are_emotions_equal(\
            stage.emotions_survey,\
            stage.reference_emotions_audio)):
                coherent_emos += 1.0
        return float(coherent_emos/float(len(game.game_stages)))

    def are_emotions_equal(self, emo1, emo2):
        for e1 in emo1:
            for e2 in emo2:
                if e1.emotion_label == e2.emotion_label:
                    return True
        return False
