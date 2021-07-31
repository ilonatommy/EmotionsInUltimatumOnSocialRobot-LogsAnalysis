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


def rgb2gray(img):
    rgb_weights = [0.2989, 0.5870, 0.1140]
    return np.dot(img[...,:3], rgb_weights)

class VideoAnalyser:
    def __init__(self):
        AI_MODELS_DIR = os.path.join(os.getcwd(), 'aiAnalysers/AI_models/video')
        with open(os.path.join(AI_MODELS_DIR, 'best.json'), 'r') as json_file:
            txt_model = json_file.read()
            self.model = model_from_json(txt_model)
            self.model.load_weights(os.path.join(AI_MODELS_DIR, 'best.hdf5'))

    def __analyse_video(self, game_logs_path, im_path):
        im = Image.open(im_path)
        arrIm = np.array(im)
        cropped_bin_versor = np.expand_dims(np.expand_dims(rgb2gray(arrIm), 2), 0)
        predictions = self.model.predict(np.asarray(cropped_bin_versor))
        predicted_emotion = np.argmax(predictions)
        current_game_video_csv = sorted(\
            glob.glob(\
                game_logs_path + '/classifiers_output/video/*'), \
                key = os.path.getmtime \
            )[-1]
        with open(current_game_video_csv, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Config().video_header)
            writer.writerow({\
            'filename': os.path.basename(im_path), \
            'max_emotion': predicted_emotion, \
            'emotion_label': Config().video_labels[predicted_emotion], \
            'AN': predictions[0][0], \
            'FE': predictions[0][1], \
            'HA': predictions[0][2], \
            'SA': predictions[0][3], \
            'SU': predictions[0][4]})

    def analyse_video_logs(self):
        for game_dir in sorted(os.listdir(Config().reanalysis_path)):
            if '.' in game_dir:
                continue
            game_logs_path = os.path.join(Config().reanalysis_path, \
            game_dir, "video_files", game_dir[:-1])
            for im in os.listdir(game_logs_path):
                self.__analyse_video(\
                    os.path.join(Config().reanalysis_path, game_dir), \
                    os.path.join(game_logs_path, im) \
                )
