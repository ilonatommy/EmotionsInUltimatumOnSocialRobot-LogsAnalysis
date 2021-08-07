from config import Config
from gameAnalyser import GameAnalyser
from models.gameModel import GameModel
from config import Config
from dataReaders.gameDataReader import GameDataReader
from dataReaders.surveyResultsDataReader import SurveyResultsDataReader
from plotter import Plotter

import os


class DataAnalyser:
    def __init__(self):
        pass

    def get_all_games_data(self):
        games = []
        for game_dir in sorted(os.listdir(Config().logs_path)):
            if '.' in game_dir:
                continue
            gdr = GameDataReader(game_dir)
            gm = gdr.read_game_data()
            games.append(gm)
        return games

    def run_logs_analysis(self, plot=False):
        games = self.get_all_games_data()
        srdr = SurveyResultsDataReader()
        survey_emotions, version_equals_opinion = srdr.read_emotion_data()
        for g_idx, g in enumerate(games):
            g.game_stages = g.update_game_stages_with_survey(g.game_stages, \
            survey_emotions[g_idx*6:(g_idx+1)*6])
            g.game_stages = g.update_game_stages_with_reference_data(g.game_stages)
        ga = GameAnalyser()
        version_counter = ga.analyse_versions(games, version_equals_opinion)

        survey_counter = ga.analyse_survey_per_class(games)
        my_ai_filtered__vs_survey_counter = ga. \
            analyse_my_ai_filtered_vs_survey_per_class(games)
        my_ai_audio_vs_survey_counter = ga. \
            analyse_my_ai_audio_vs_survey_per_class(games)
        my_ai_video_vs_survey_counter = ga. \
            analyse_my_ai_video_vs_survey_per_class(games)

        ref_ai_vs_survey_counter = ga. \
            analyse_reference_ai_filtered_vs_survey_per_class(games)
        ref_ai_audio_vs_survey_counter = ga. \
            analyse_reference_ai_audio_vs_survey_per_class(games)
        ref_ai_video_vs_survey_counter = ga. \
            analyse_reference_ai_video_vs_survey_per_class(games)

        my_ai_filtered_vs_survey = "My AI filtered vs survey"
        my_ai_audio_vs_survey = "My AI audio vs survey"
        my_ai_video_vs_survey = "My AI video vs survey"

        ref_ai_vs_survey = "Reference AI filtered vs survey"
        ref_ai_audio_vs_survey = "Reference AI audio vs survey"
        ref_ai_video_vs_survey = "Reference AI video vs survey"

        survey = "Survey stats"

        print("\n{0}: {1}\n{2}: {3}\n{4}: {5}\n{6}: {7}\n{8}: {9}\n{10}: {11}\n".format(\
            my_ai_filtered_vs_survey, \
            my_ai_filtered__vs_survey_counter, \

            my_ai_audio_vs_survey, \
            my_ai_audio_vs_survey_counter, \

            my_ai_video_vs_survey, \
            my_ai_video_vs_survey_counter, \

            ref_ai_vs_survey, \
            ref_ai_vs_survey_counter, \

            ref_ai_audio_vs_survey, \
            ref_ai_audio_vs_survey_counter, \

            ref_ai_video_vs_survey, \
            ref_ai_video_vs_survey_counter, \
        ))

        if plot:
            p = Plotter(Config().plot_results_path, False)
            p.plot_info_model(version_counter, "Versions vs survey opinions")
            p.plot_info_model(survey_counter, "Survey")
            p.plot_info_model(my_ai_filtered__vs_survey_counter, \
                "My AI: filtered vs survey")
            p.plot_info_model(my_ai_audio_vs_survey_counter, \
                "My AI: audio vs survey")
            p.plot_info_model(my_ai_video_vs_survey_counter, \
                "My AI: video vs survey")
            p.plot_info_model(ref_ai_vs_survey_counter, \
                "Reference AI: filtered vs survey")
            p.plot_info_model(ref_ai_audio_vs_survey_counter, \
                "Reference AI: audio vs survey")
            p.plot_info_model(ref_ai_video_vs_survey_counter, \
                "Reference AI: video vs survey")

        my_ai_filtered__vs_survey_counter.count2percentage()
        my_ai_audio_vs_survey_counter.count2percentage()
        my_ai_video_vs_survey_counter.count2percentage()
        ref_ai_vs_survey_counter.count2percentage()
        ref_ai_audio_vs_survey_counter.count2percentage()
        ref_ai_video_vs_survey_counter.count2percentage()
        survey_counter.count2percentage()

        print("\n{0}: {1}\n{2}: {3}\n{4}: {5}\n{6}: {7}\n{8}: {9}\n{10}: {11}\n\n{12}: {13}".format(\
            my_ai_filtered_vs_survey, \
            my_ai_filtered__vs_survey_counter, \

            my_ai_audio_vs_survey, \
            my_ai_audio_vs_survey_counter, \

            my_ai_video_vs_survey, \
            my_ai_video_vs_survey_counter, \

            ref_ai_vs_survey, \
            ref_ai_vs_survey_counter, \

            ref_ai_audio_vs_survey, \
            ref_ai_audio_vs_survey_counter, \

            ref_ai_video_vs_survey, \
            ref_ai_video_vs_survey_counter, \

            survey, \
            survey_counter, \
        ))
