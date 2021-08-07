from config import Config
from models.emotionsStatisticalInfoModel import EmotionsStatisticalInfoModel
from models.gameVersionsStatisticalInfoModel import GameVersionsStatisticalInfoModel

import copy
import numpy as np


class GameAnalyser:
    def __init__(self):
        pass

    def analyse_versions(self, games, version_equals_opinion):
        version_counter = GameVersionsStatisticalInfoModel()
        for (game, veo) in zip(games, version_equals_opinion):
            version_counter.add_version_sample(game.version)
            if veo:
                version_counter.add_success_versions_sample(game.version)
        return version_counter

    def analyse_survey_per_class(self, games):
        survey_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                for survey_emo in stage.emotions_survey:
                    survey_counter.add_class_sample(survey_emo.emotion_label)
        return survey_counter

    def analyse_my_ai_filtered_vs_survey_per_class(self, games):
        filtered_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                filtered_counter.add_class_sample( \
                    stage.sensor_filterd_emotion.emotion_label)
                if(self.is_emotion_equal_survey(\
                    stage.emotions_survey,\
                    stage.sensor_filterd_emotion)):
                    filtered_counter.add_correct_class_sample( \
                        stage.sensor_filterd_emotion.emotion_label)
        return filtered_counter

    def analyse_my_ai_audio_vs_survey_per_class(self, games):
        audio_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                for emotion in stage.emotions_audio:
                    audio_counter.add_class_sample( \
                        emotion.emotion_label)
                    if(self.is_emotion_equal_survey( \
                        stage.emotions_survey,
                        emotion)):
                        audio_counter.add_correct_class_sample( \
                            emotion.emotion_label)
        return audio_counter

    def analyse_my_ai_video_vs_survey_per_class(self, games):
        video_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                for emotion in stage.emotions_video:
                    video_counter.add_class_sample( \
                        emotion.emotion_label)
                    if(self.is_emotion_equal_survey( \
                        stage.emotions_survey,
                        emotion)):
                        video_counter.add_correct_class_sample( \
                            emotion.emotion_label)
        return video_counter

    def analyse_reference_ai_filtered_vs_survey_per_class(self, games):
        filtered_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                filtered_counter.add_class_sample( \
                    stage.reference_filterd_emotion.emotion_label)
                if(self.is_emotion_equal_survey(\
                    stage.emotions_survey,\
                    stage.reference_filterd_emotion)):
                    filtered_counter.add_correct_class_sample( \
                        stage.reference_filterd_emotion.emotion_label)
        return filtered_counter

    def analyse_reference_ai_audio_vs_survey_per_class(self, games):
        audio_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                for emotion in stage.reference_emotions_audio:
                    audio_counter.add_class_sample( \
                        emotion.emotion_label)
                    if(self.is_emotion_equal_survey( \
                        stage.emotions_survey,
                        emotion)):
                        audio_counter.add_correct_class_sample( \
                            emotion.emotion_label)
        return audio_counter

    def analyse_reference_ai_video_vs_survey_per_class(self, games):
        video_counter = EmotionsStatisticalInfoModel()
        for game in games:
            for stage in game.game_stages:
                for emotion in stage.reference_emotions_video:
                    video_counter.add_class_sample( \
                        emotion.emotion_label)
                    if(self.is_emotion_equal_survey( \
                        stage.emotions_survey,
                        emotion)):
                        video_counter.add_correct_class_sample( \
                            emotion.emotion_label)
        return video_counter

    def is_emotion_equal_survey(self, survey, emotion):
        for s in survey:
            if s.emotion_label == emotion.emotion_label:
                return True
        return False
