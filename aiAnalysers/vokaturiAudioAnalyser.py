from config import Config

import os
import csv
import glob
import sys
import scipy
import numpy as np
sys.path.append("aiAnalysers/reference_AI_models/audio/api")
from reference_AI_models.audio.api.Vokaturi import *

# CODE IN THIS FILE ORIGINATES FROM PYTHON LIBRARY: https://vokaturi.com/
# reported acc on the five built-in emotions is 76.1%


class VakaturiAudioAnalyser:
    def __init__(self):
        load("aiAnalysers/reference_AI_models/audio/lib/open/linux/OpenVokaturi-3-4-linux64.so")

    def __analyse_audio(self, current_game_audio_csv, rec_path):
        try:
            (sample_rate, samples) = scipy.io.wavfile.read(rec_path)
            buffer_length = len(samples)
            c_buffer = SampleArrayC(buffer_length)
            if samples.ndim == 1:  # mono
            	c_buffer[:] = samples[:] / 32768.0
            else:  # stereo
            	c_buffer[:] = 0.5*(samples[:,0]+0.0+samples[:,1]) / 32768.0
            voice = Voice (sample_rate, buffer_length)
            voice.fill(buffer_length, c_buffer)
            quality = Quality()
            emotion_probabilities = EmotionProbabilities()
            voice.extract(quality, emotion_probabilities)
            with open(current_game_audio_csv, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=Config().audio_reanalysis_header)
                predictions = [
                    emotion_probabilities.anger,
                    emotion_probabilities.fear,
                    emotion_probabilities.happiness,
                    emotion_probabilities.neutrality,
                    emotion_probabilities.sadness
                ]
                predicted_emotion = np.argmax(predictions)
                if quality.valid:
                    writer.writerow({\
                        'filename': os.path.basename(rec_path), \
                        'max_emotion': predicted_emotion, \
                        'emotion_label': Config().vokaturi_labels[predicted_emotion], \
                        'AN': predictions[0], \
                        'FE': predictions[1], \
                        'HA': predictions[2], \
                        'NE': predictions[3], \
                        'SA': predictions[4]})
            voice.destroy()
        except Exception, e:
            print('{0}\n{1}'.format(rec_path, e))

    def analyse_audio_logs(self):
        self.clean_audio_logs()
        for game_dir in sorted(os.listdir(Config().reanalysis_path)):
            if '.' in game_dir:
                continue
            game_data_path = os.path.join(Config().reanalysis_path, \
            game_dir, "audio_files", game_dir[:-1])
            game_logs_path = os.path.join(Config().reanalysis_path, game_dir)
            current_game_audio_csv = os.path.join(
                game_logs_path, \
                Config().audio_classifier_path,
                os.path.basename(os.path.normpath(game_logs_path) + ".csv")
                )
            with open(current_game_audio_csv, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=Config().audio_reanalysis_header)
                writer.writeheader()
            for rec in os.listdir(game_data_path):
                self.__analyse_audio(\
                    current_game_audio_csv, \
                    os.path.join(game_data_path, rec) \
                )

    def clean_audio_logs(self):
        for game_dir in sorted(os.listdir(Config().reanalysis_path)):
            if '.' in game_dir:
                continue
            game_logs_path = os.path.join(Config().reanalysis_path, \
            game_dir, Config().audio_classifier_path)
            for result_csv in  os.listdir(game_logs_path):
                os.remove(os.path.join(game_logs_path, result_csv))
