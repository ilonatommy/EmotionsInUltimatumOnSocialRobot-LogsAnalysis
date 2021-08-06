from config import Config
from gameAnalyser import GameAnalyser
from models.gameModel import GameModel
from config import Config
from dataReaders.gameDataReader import GameDataReader
from dataReaders.surveyResultsDataReader import SurveyResultsDataReader

import os


class DataAnalyser:
    def __init__(self):
        pass

    def __get_success_rate(self, games, comparison_method):
        ga = GameAnalyser()
        percentage = 0.0
        for game in games:
            percentage += \
                comparison_method(game)
        return float(percentage/len(games))

    def get_all_games_data(self):
        games = []
        for game_dir in sorted(os.listdir(Config().logs_path)):
            if '.' in game_dir:
                continue
            gdr = GameDataReader(game_dir)
            gm = gdr.read_game_data()
            games.append(gm)
        return games

    def run_logs_analysis(self):
        games = self.get_all_games_data()
        srdr = SurveyResultsDataReader()
        survey_emotions = srdr.read_emotion_data()
        for g_idx, g in enumerate(games):
            g.game_stages = g.update_game_stages_with_survey(g.game_stages, \
            survey_emotions[g_idx*6:(g_idx+1)*6])
            g.game_stages = g.update_game_stages_with_reference_data(g.game_stages)
        ga = GameAnalyser()

        my_ai_filtered_vs_survey_success_rate = \
            self.__get_success_rate(games, \
            ga.get_my_ai_filtered_vs_survey_coherent_emotions_percentage)
        my_ai_audio_vs_survey_success_rate = \
            self.__get_success_rate(games, \
            ga.get_my_ai_audio_vs_survey_coherent_emotions_percentage)
        my_ai_video_vs_survey_success_rate = \
            self.__get_success_rate(games, \
            ga.get_my_ai_audio_vs_survey_coherent_emotions_percentage)

        ref_ai_vs_survey_success_rate = \
            self.__get_success_rate(games, \
            ga.get_reference_ai_vs_survey_coherent_emotions_percentage)
        ref_ai_audio_vs_survey_success_rate = \
            self.__get_success_rate(games, \
            ga.get_reference_ai_audio_vs_survey_coherent_emotions_percentage)
        ref_ai_video_vs_survey_success_rate = \
            self.__get_success_rate(games, \
            ga.get_reference_ai_video_vs_survey_coherent_emotions_percentage)

        my_ai_filtered_vs_survey = "My AI filtered vs survey acc"
        my_ai_audio_vs_survey = "My AI audio vs survey acc"
        my_ai_video_vs_survey = "My AI video vs survey acc"

        ref_ai_vs_survey = "Reference AI filtered vs survey acc"
        ref_ai_audio_vs_survey = "Reference AI audio vs survey acc"
        ref_ai_video_vs_survey = "Reference AI video vs survey acc"
        print("{0}: {1}\n{2}: {3}\n{4}: {5}\n{6}: {7}\n{8}: {9}\n{10}: {11}".format(\
            my_ai_filtered_vs_survey, \
            my_ai_filtered_vs_survey_success_rate, \

            my_ai_audio_vs_survey, \
            my_ai_audio_vs_survey_success_rate, \

            my_ai_video_vs_survey, \
            my_ai_video_vs_survey_success_rate, \

            ref_ai_vs_survey, \
            ref_ai_vs_survey_success_rate, \

            ref_ai_audio_vs_survey, \
            ref_ai_audio_vs_survey_success_rate, \

            ref_ai_video_vs_survey, \
            ref_ai_video_vs_survey_success_rate))
