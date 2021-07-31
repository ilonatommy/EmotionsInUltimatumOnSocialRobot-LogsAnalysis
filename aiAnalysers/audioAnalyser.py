from config import Config

import re
import os
import csv
from datetime import datetime
import numpy as np
from tensorflow.keras.models import model_from_json
import librosa
import glob


class AudioAnalyser:
    def __init__(self):
        AI_MODELS_DIR = os.path.join(os.getcwd(), 'aiAnalysers/AI_models/audio')
        with open(os.path.join(AI_MODELS_DIR, 'best.json'), 'r') as json_file:
            txt_model = json_file.read()
            self.model = model_from_json(txt_model)
            self.model.load_weights(os.path.join(AI_MODELS_DIR, 'best.hdf5'))


    def __extract_features(self, data, sr):
        # ZCR
        result = np.array([])
        zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
        result=np.hstack((result, zcr)) # stacking horizontally

        # Chroma_stft
        stft = np.abs(librosa.stft(data))
        chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr).T, axis=0)
        result = np.hstack((result, chroma_stft)) # stacking horizontally

        # MFCC
        mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sr).T, axis=0)
        result = np.hstack((result, mfcc)) # stacking horizontally

        # Root Mean Square Value
        rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
        result = np.hstack((result, rms)) # stacking horizontally

        # MelSpectogram
        mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sr).T, axis=0)
        result = np.hstack((result, mel)) # stacking horizontally

        return np.expand_dims(np.array(result), axis=-1)


    def __analyse_audio(self, game_logs_path, rec_path):
        data, sr = librosa.load(rec_path)
        audio_features = self.__extract_features(data, sr)
        predictions = self.model.predict(np.expand_dims(audio_features, axis=0))
        predicted_emotion = np.argmax(predictions)
        current_game_audio_csv = sorted(\
            glob.glob(\
                game_logs_path + '/classifiers_output/audio/*'), \
                key = os.path.getmtime \
            )[-1]
        with open(current_game_audio_csv, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Config().audio_header)
            writer.writerow({\
            'filename': os.path.basename(rec_path), \
            'max_emotion': predicted_emotion, \
            'emotion_label': Config().audio_labels[predicted_emotion], \
            'AN': predictions[0][0], \
            'DI': predictions[0][1], \
            'FE': predictions[0][2], \
            'HA': predictions[0][3], \
            'NE': predictions[0][4], \
            'SA': predictions[0][5]})

    def analyse_audio_logs(self):
        for game_dir in sorted(os.listdir(Config().reanalysis_path)):
            if '.' in game_dir:
                continue
            game_logs_path = os.path.join(Config().reanalysis_path, \
            game_dir, "audio_files", game_dir[:-1])
            for rec in os.listdir(game_logs_path):
                self.__analyse_audio(\
                    os.path.join(Config().reanalysis_path, game_dir), \
                    os.path.join(game_logs_path, rec) \
                )
