from datetime import datetime
from gameStageModel import GameStageModel
from enums.gameVersionEnum import GameVersionEnum

class GameModel:
    def __init__(self, game_timestamp, game_stages, version = GameVersionEnum.UNDEFINED):
        # type: (GameModel, datetime, [GameStageModel], GameVersionEnum) -> None:
        self.game_timestamp = game_timestamp
        self.game_stages = game_stages
        self.version = version
