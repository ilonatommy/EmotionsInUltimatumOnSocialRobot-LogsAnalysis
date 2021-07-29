class Config:
    def __init__(self):
        self.logs_path = "logs"
        self.audio_classifier_path = "classifiers_output/audio"
        self.video_classifier_path = "classifiers_output/video"
        self.stages_log_file_name = "eventsModule.log"
        self.audio_header = ['filename', 'max_emotion', 'emotion_label', 'AN', \
        'DI', 'FE', 'HA', 'NE', 'SA']
        self.video_header = ['filename', 'max_emotion', 'emotion_label', 'AN', \
        'FE', 'HA', 'SA', 'SU']
        # [
        #  beforeGame
        #  afterFirstRobotSentence
        #  after1stRound
        #  after2ndRound
        #  after3rdRound
        #  after4thRound
        # ]
        self.game_stages = [
        'askIfWantsToPlay', \
        'onStartRound1', \
        'onStartRound2', \
        'askIfToContinue', \
        'onStartRound4', \
        'gameEnd' \
        ]
