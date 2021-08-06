from config import Config
from enums.emotionSourceEnum import EmotionSourceEnum
from models.emotionModel import EmotionModel

import re
import os
import csv
from datetime import datetime
import numpy as np


class EmotionsDataReader:
    def __init__(self, game_dir_name, emotion_source, logs_path=Config().logs_path):
        self.logs_path = logs_path
        self.game_dir_name = game_dir_name
        self.emotion_source = emotion_source
        self.are_data_from_reference_models = logs_path != Config().logs_path
        if self.are_data_from_reference_models:
            if emotion_source == EmotionSourceEnum.AUDIO:
                self.classifier_path = Config().audio_classifier_path
                self.header = Config().audio_reanalysis_header
            if emotion_source == EmotionSourceEnum.VIDEO:
                self.classifier_path = Config().video_classifier_path
                self.header = Config().video_reanalysis_header
        else:
            if emotion_source == EmotionSourceEnum.AUDIO:
                self.classifier_path = Config().audio_classifier_path
                self.header = Config().audio_header
            if emotion_source == EmotionSourceEnum.VIDEO:
                self.classifier_path = Config().video_classifier_path
                self.header = Config().video_header

    def __read_standard_data(self, source_csv):
        emotions = []
        with open(source_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                probabilities = []
                for label in self.header[3:]:
                    probabilities.append(float(row[label]))
                unified_probabilities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                if self.emotion_source == EmotionSourceEnum.AUDIO:
                    unified_probabilities[:-1] = probabilities
                else:
                    unified_probabilities[0] = probabilities[0]
                    unified_probabilities[2:4] = probabilities[1:3]
                    unified_probabilities[5:] = probabilities[-2:]
                max_emotion = np.argmax(unified_probabilities)
                timestamp = datetime.strptime(row['filename'][:-11], '%Y-%b-%d_%H:%M:%S')
                emotion = EmotionModel(timestamp, self.emotion_source, \
                     row['filename'], max_emotion, \
                     np.array(unified_probabilities), row['emotion_label'])
                emotions.append(emotion)
        return emotions

    def __read_reference_data(self, source_csv):
        emotions = []
        with open(source_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                probabilities = []
                for label in self.header[3:]:
                    probabilities.append(float(row[label]))
                unified_probabilities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                if self.emotion_source == EmotionSourceEnum.AUDIO:
                    unified_probabilities[0] = probabilities[0]
                    unified_probabilities[2] = probabilities[1]
                    unified_probabilities[3] = probabilities[2]
                    unified_probabilities[4] = probabilities[3]
                    unified_probabilities[5] = probabilities[4]
                else:
                    unified_probabilities[0:4] = probabilities[0:4]
                    unified_probabilities[4] = probabilities[6]
                    unified_probabilities[5] = probabilities[4]
                    unified_probabilities[6] = probabilities[5]
                max_emotion = np.argmax(unified_probabilities)
                timestamp = datetime.strptime(row['filename'][:-11], '%Y-%b-%d_%H:%M:%S')
                emotion = EmotionModel(timestamp, self.emotion_source, \
                     row['filename'], max_emotion, \
                     np.array(unified_probabilities), row['emotion_label'])
                emotions.append(emotion)
        return emotions

    def read_emotion_data(self):
        results_path = os.path.join(self.logs_path, self.game_dir_name, \
            self.classifier_path)
        source_csv = os.path.join(results_path, os.listdir(results_path)[0])
        if self.are_data_from_reference_models:
            return self.__read_reference_data(source_csv)
        return self.__read_standard_data(source_csv)
