from datetime import datetime
from models.emotionModel import EmotionModel

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
