from config import Config
from enums.emotionSourceEnum import EmotionSourceEnum
from models.emotionModel import EmotionModel

import re
import os
import csv
from datetime import datetime


class EmotionsDataReader:
    def __init__(self, game_dir_name, emotion_source):
        self.game_dir_name = game_dir_name
        self.emotion_source = emotion_source
        if emotion_source == EmotionSourceEnum.AUDIO:
            self.classifier_path = Config().audio_classifier_path
            self.header = Config().audio_header
        else:
            self.classifier_path = Config().video_classifier_path
            self.header = Config().video_header

    def read_emotion_data(self):
        emotions = []
        results_path = os.path.join(Config().logs_path, self.game_dir_name, \
        self.classifier_path)
        csv_file = os.listdir(results_path)[0]
        with open(os.path.join(results_path, csv_file), 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                probabilities = []
                for label in self.header[4:]:
                    probabilities.append(float(row[label]))
                timestamp = datetime.strptime(row['filename'][:-11], '%Y-%b-%d_%H:%M:%S')
                emotion = EmotionModel(timestamp, self.emotion_source, \
                     row['filename'], row['max_emotion'], probabilities, row['emotion_label'])
                emotions.append(emotion)
        return emotions
