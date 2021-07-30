from config import Config
from enums.gameVersionEnum import GameVersionEnum
from models.gameModel import GameModel
from dataReaders.stageDataReader import StageDataReader
from dataReaders.surveyResultsDataReader import SurveyResultsDataReader

from datetime import datetime


class GameDataReader:
    def __init__(self, game_dir_name):
        self.game_dir_name = game_dir_name

    def __get_game_version(self):
        game_version = GameVersionEnum.UNDEFINED
        version_sign = self.game_dir_name[-1]
        if not version_sign.isdigit():
            if version_sign == "+":
                game_version = GameVersionEnum.EMPHATIC
            if version_sign == "-":
                game_version = GameVersionEnum.EGOISTIC
        return game_version

    def __get_game_timestamp(self):
        last_char = self.game_dir_name[-1]
        if last_char.isdigit():
            return datetime.strptime(self.game_dir_name, '%Y-%b-%d_%H:%M:%S')
        else:
            return datetime.strptime(self.game_dir_name[:-1], '%Y-%b-%d_%H:%M:%S')

    def __update_game_stages_with_survey(self, game_stages, survey_emotions):
        for stage, emo in zip(game_stages, survey_emotions):
            stage.emotions_survey.append(emo)
        return game_stages

    def read_game_data(self):
        game_timestamp = self.__get_game_timestamp()
        sdr = StageDataReader(self.game_dir_name)
        game_stages = sdr.read_stages_data(game_timestamp)
        srdr = SurveyResultsDataReader()
        survey_emotions = srdr.read_emotion_data()
        game_stages = self.__update_game_stages_with_survey(game_stages, survey_emotions)
        game_version = self.__get_game_version()
        gm = GameModel(game_timestamp, game_stages, game_version)
        return gm
