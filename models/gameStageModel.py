from models.emotionModel import EmotionModel
from enums.emotionSourceEnum import EmotionSourceEnum

from datetime import datetime


class GameStageModel:
    def __init__(self, stage_name, stage_id, start_time, end_time, emotions_video, emotions_audio, emotions_survey):
        # type: (GameStageModel, str, int, datetime, datetime, [EmotionModel], [EmotionModel], [EmotionModel]) -> None:
        self.stage_name = stage_name
        self.stage_id = stage_id
        self.start_time = start_time
        self.end_time = end_time
        self.emotions_video = emotions_video
        self.emotions_audio = emotions_audio
        self.emotions_survey = emotions_survey

    def __repr__(self):
        return '\n\n{stage_name} ({start_time} - {end_time})\n{video_source}: ''{emotions_video}\n{audio_source}: {emotions_audio}\n{survey_source}: {emotions_survey}\n'.format(\
        stage_name=self.stage_name, \
        start_time=self.start_time, \
        end_time=self.end_time, \
        video_source=EmotionSourceEnum.VIDEO, \
        emotions_video=self.emotions_video, \
        audio_source=EmotionSourceEnum.AUDIO, \
        emotions_audio=self.emotions_audio, \
        survey_source=EmotionSourceEnum.SURVEY, \
        emotions_survey=self.emotions_survey)

    def __str__(self):
        return '\n\n{stage_name} ({start_time} - {end_time})\n{video_source}: ''{emotions_video}\n{audio_source}: {emotions_audio}\n{survey_source}: {emotions_survey}\n'.format(\
        stage_name=self.stage_name, \
        start_time=self.start_time, \
        end_time=self.end_time, \
        video_source=EmotionSourceEnum.VIDEO, \
        emotions_video=self.emotions_video, \
        audio_source=EmotionSourceEnum.AUDIO, \
        emotions_audio=self.emotions_audio, \
        survey_source=EmotionSourceEnum.SURVEY, \
        emotions_survey=self.emotions_survey)
