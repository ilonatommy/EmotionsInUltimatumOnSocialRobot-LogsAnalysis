from config import Config
from gameStageModel import GameStageModel
from enums.gameVersionEnum import GameVersionEnum
from dataReaders.stageDataReader import StageDataReader
from helpers import *


class GameModel:
    def __init__(self, game_timestamp, game_stages, version = GameVersionEnum.UNDEFINED):
        # type: (GameModel, datetime, [GameStageModel], GameVersionEnum) -> None:
        self.game_timestamp = game_timestamp
        self.game_stages = game_stages
        self.version = version

    def __repr__(self):
        return '{version} {game_timestamp} {game_stages})'.format(\
        version=self.version, \
        game_timestamp=self.game_timestamp, \
        game_stages=self.game_stages)

    def __str__(self):
        return '{version} {game_timestamp} {game_stages})'.format(\
        version=self.version, \
        game_timestamp=self.game_timestamp, \
        game_stages=self.game_stages)

    def update_game_stages_with_survey(self, game_stages, survey_emotions):
        for stage, emo in zip(game_stages, survey_emotions):
            stage.emotions_survey = emo
        return game_stages

    def update_game_stages_with_reference_data(self, game_stages):
        game_dir_name = timestamp2str(self.game_timestamp) + \
            version2str(self.version)
        for stage in game_stages:
            sdr = StageDataReader(game_dir_name, Config().reanalysis_path)
            stage = sdr.update_stage_with_reference_audio_data(stage)
        return game_stages
