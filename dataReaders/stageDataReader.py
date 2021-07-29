from config import Config
from enums.emotionSourceEnum import EmotionSourceEnum
from models.gameStageModel import GameStageModel
from dataReaders.emotionsDataReader import EmotionsDataReader

import re
import os
from datetime import datetime


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
        audio_edr = EmotionsDataReader(self.game_dir_name, EmotionSourceEnum.AUDIO)
        emotions_audio = audio_edr.read_emotion_data()
        video_edr = EmotionsDataReader(self.game_dir_name, EmotionSourceEnum.VIDEO)
        emotions_video = video_edr.read_emotion_data()
        meaningful_stage_id = 0

        for l in lines:
            if l.isspace():
                continue
            stage_name_area = re.findall(r"reached game point: .*", l)
            stage_name = stage_name_area[0][20:]
            if Config().game_stages[meaningful_stage_id] == stage_name:
                meaningful_stage_id += 1
                if stage_id != 0:
                    start_time = end_time
                timestamp_area = re.findall(r"; on \[.*] - reached game point:", l)
                end_time_str = re.findall(r"\[.*]", timestamp_area[0])[0][1:-1]
                end_time = datetime.strptime(end_time_str, '%Y-%b-%d_%H:%M:%S')
                video_emo = filter(lambda x: x.emotion_timestamp >= start_time and \
                x.emotion_timestamp < end_time, emotions_video)
                audio_emo = filter(lambda x: x.emotion_timestamp >= start_time and \
                x.emotion_timestamp < end_time, emotions_audio)
                gsm = GameStageModel(stage_name, stage_id, start_time, end_time, video_emo, audio_emo, [])
                game_stage_models.append(gsm)
                stage_id += 1
        return game_stage_models
