from models.gameModel import GameModel
from config import Config
from dataReaders.gameDataReader import GameDataReader
from statistics.dataAnalyser import DataAnalyser

import os


def main():
    games = []
    for game_dir in sorted(os.listdir(Config().logs_path)):
        if '.' in game_dir:
            continue
        gdr = GameDataReader(game_dir)
        gm = gdr.read_game_data()
        games.append(gm)
    da = DataAnalyser()
    survey_success_rate = da.get_games_stats(games)
    print(survey_success_rate)


if __name__ == "__main__":
    main()
