from config import Config
from enums.emotionSourceEnum import EmotionSourceEnum
from models.emotionModel import EmotionModel

import re
import os
import csv
from datetime import datetime
import numpy as np
from tensorflow.keras.models import model_from_json
import librosa
import glob
from PIL import Image
from tensorflow.keras.models import load_model


def rgb2gray(img):
    rgb_weights = [0.2989, 0.5870, 0.1140]
    return np.dot(img[...,:3], rgb_weights)

class MERVideoAnalyser:
    def __init__(self):
        AI_MODEL = os.path.join(os.getcwd(), './aiAnalysers/reference_AI_models/video/video.h5')
        self.model = load_model(AI_MODEL, compile=False)

    def __analyse_video(self, current_game_video_csv, im_path):
        im = Image.open(im_path)
        im48x48 = im.resize((48, 48), Image.ANTIALIAS)
        im48x48.save('somepic.jpg')
        arrIm = rgb2gray(np.array(im48x48))
        cropped_bin_versor = np.reshape(arrIm.flatten(), (1, 48, 48, 1))
        predictions = self.model.predict(cropped_bin_versor)
        predicted_emotion = np.argmax(predictions)
        with open(current_game_video_csv, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Config().video_reanalysis_header)
            writer.writerow({\
            'filename': os.path.basename(im_path), \
            'max_emotion': predicted_emotion, \
            'emotion_label': Config().mer_labels[predicted_emotion], \
            'AN': predictions[0][0], \
            'DI': predictions[0][1], \
            'FE': predictions[0][2], \
            'HA': predictions[0][3], \
            'SA': predictions[0][4], \
            'SU': predictions[0][5],
            'NE': predictions[0][6]})

    def analyse_video_logs(self):
        self.clean_video_logs()
        for game_dir in sorted(os.listdir(Config().reanalysis_path)):
            if '.' in game_dir:
                continue
            game_data_path = os.path.join(Config().reanalysis_path, \
            game_dir, "video_files", game_dir[:-1])
            game_logs_path = os.path.join(Config().reanalysis_path, game_dir)
            current_game_video_csv = os.path.join(
                game_logs_path, \
                Config().video_classifier_path,
                os.path.basename(os.path.normpath(game_logs_path) + ".csv")
                )
            with open(current_game_video_csv, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=Config().video_reanalysis_header)
                writer.writeheader()
            for rec in os.listdir(game_data_path):
                self.__analyse_video(\
                    current_game_video_csv, \
                    os.path.join(game_data_path, rec) \
                )

    def clean_video_logs(self):
        for game_dir in sorted(os.listdir(Config().reanalysis_path)):
            if '.' in game_dir:
                continue
            game_logs_path = os.path.join(Config().reanalysis_path, \
            game_dir, Config().video_classifier_path)
            for result_csv in  os.listdir(game_logs_path):
                os.remove(os.path.join(game_logs_path, result_csv))
