from config import Config
from statistics.gameAnalyser import GameAnalyser


class DataAnalyser:
    def __init__(self):
        pass

    def get_games_stats(self, games):
        ga = GameAnalyser()
        percentage = 0.0
        for game in games:
            percentage += ga.get_coherent_emotions_percentage(game)
        survey_success_rate = float(percentage/len(games))
        return survey_success_rate
