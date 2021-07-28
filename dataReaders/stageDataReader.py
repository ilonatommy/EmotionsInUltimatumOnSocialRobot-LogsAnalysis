from config import Config
from enums.emotionSourceEnum import EmotionSourceEnum
from models.gameStageModel import GameStageModel

import re
import os

class StageDataReader:
    def __init__(self, game_dir_name):
        self.game_dir_name = game_dir_name

    def __read_file_lines(self, file_name):
        stages_file = os.path.join(Config().logs_path, self.game_dir_name, \
        file_name)
        with open(stages_file, 'r') as f:
            file_lines = f.readlines()
        return file_lines

    def read_stages_data(self, game_timestamp):
        start_time = game_timestamp
        end_time = game_timestamp
        lines = self.__read_file_lines(Config().stages_log_file_name)
        stage_id = 0
        game_stage_models = []

        for l in lines:
            if l.isspace():
                continue
            if stage_id != 0:
                start_time = end_time
            timestamp_area = re.findall(r"; on \[.*] - reached game point:", l)
            end_time = re.findall(r"\[.*]", timestamp_area[0])[0][1:-1]
            stage_name_area = re.findall(r"reached game point: .*", l)
            stage_name = stage_name_area[0][20:]
            gsm = GameStageModel(stage_name, stage_id, start_time, end_time, [], [], [])
            game_stage_models.append(gsm)
            stage_id += 1
