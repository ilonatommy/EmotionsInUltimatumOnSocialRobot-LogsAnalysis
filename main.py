from models.gameModel import GameModel
from config import Config
from dataReaders.gameDataReader import GameDataReader

import os


def main():
    for game_dir in sorted(os.listdir(Config().logs_path)):
        gdr = GameDataReader(game_dir)
        gm = gdr.read_game_data()
        break


if __name__ == "__main__":
    main()
