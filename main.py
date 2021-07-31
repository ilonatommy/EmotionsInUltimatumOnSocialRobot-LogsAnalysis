from models.gameModel import GameModel
from config import Config
from dataReaders.gameDataReader import GameDataReader
from statistics.dataAnalyser import DataAnalyser
from dataReaders.surveyResultsDataReader import SurveyResultsDataReader

import os


def main():
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
    da = DataAnalyser()
    survey_success_rate = da.get_games_stats(games)
    print(survey_success_rate)


if __name__ == "__main__":
    main()
# nie wpisuja sie emocje do emotions_survey w stage.
