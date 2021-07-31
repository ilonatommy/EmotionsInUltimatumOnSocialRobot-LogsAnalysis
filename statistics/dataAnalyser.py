from config import Config
from statistics.gameAnalyser import GameAnalyser
from models.gameModel import GameModel
from config import Config
from dataReaders.gameDataReader import GameDataReader
from dataReaders.surveyResultsDataReader import SurveyResultsDataReader

import os


class DataAnalyser:
    def __init__(self):
        pass

    def __get_games_stats(self, games):
        ga = GameAnalyser()
        percentage = 0.0
        for game in games:
            percentage += ga.get_coherent_emotions_percentage(game)
        survey_success_rate = float(percentage/len(games))
        return survey_success_rate

    def run_logs_analysis(self):
        games = []
        i = 0
        for game_dir in sorted(os.listdir(Config().logs_path)):
            if '.' in game_dir:
                continue
            gdr = GameDataReader(game_dir)
            gm = gdr.read_game_data()
            games.append(gm)
        srdr = SurveyResultsDataReader()
        survey_emotions = srdr.read_emotion_data()
        for g_idx, g in enumerate(games):
            g.game_stages = g.update_game_stages_with_survey(g.game_stages, \
            survey_emotions[g_idx*6:(g_idx+1)*6])
        surveys_success_rate = self.__get_games_stats(games)
        return surveys_success_rate
