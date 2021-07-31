from config import Config
from enums.emotionSourceEnum import EmotionSourceEnum
from models.emotionModel import EmotionModel

import re
import os
import csv
from datetime import datetime
import numpy as np


class SurveyResultsDataReader:
    def __init__(self):
        self.header = Config().survey_header

    def read_emotion_data(self):
        emotions = []
        csv_file = os.path.join(Config().logs_path, \
        Config().survey_file_name)
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                timestamp = datetime.strptime(row['timestamp'], '%Y-%b-%d_%H:%M:%S')
                for stage_idx, stage in enumerate(Config().game_stages):
                    probabilities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                    max_emo = row[str(stage_idx + 1)]
                    next_max_emo = row[str(stage_idx + 1) + "a"]
                    max_emo_percentage = 1.0
                    emotion = []
                    if next_max_emo != "":
                        max_emo_percentage = 0.7
                        probabilities[int(Config().emotion_indices[Config().\
                        survey_labels_dict[max_emo]])] = max_emo_percentage
                        probabilities[int(Config().emotion_indices[Config().\
                        survey_labels_dict[next_max_emo]])] = 1.0 - max_emo_percentage

                    else:
                        probabilities[int(Config().emotion_indices[Config().\
                        survey_labels_dict[max_emo]])] = max_emo_percentage
                    emotion.append(
                        EmotionModel(timestamp, EmotionSourceEnum.SURVEY, \
                        "", row['1'], np.array(probabilities), \
                        Config().survey_labels_dict[max_emo]),
                    )
                    if next_max_emo != "":
                        emotion.append(
                            EmotionModel(timestamp, EmotionSourceEnum.SURVEY, \
                            "", row['1'], np.array(probabilities), \
                            Config().survey_labels_dict[next_max_emo])
                        )
                    emotions.append(emotion)
        return emotions
