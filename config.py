class Config:
    def __init__(self):
        self.audio_ratio = 0.3
        self.emotion_labels = {
        0: 'AN',
        1: 'DI',
        2: 'FE',
        3: 'HA',
        4: 'NE',
        5: 'SA',
        6: 'SU'
        }
        self.emotion_indices = {
        'AN': 0,
        'DI': 1,
        'FE': 2,
        'HA': 3,
        'NE': 4,
        'SA': 5,
        'SU': 6
        }
        self.logs_path = "logs"
        self.audio_classifier_path = "classifiers_output/audio"
        self.video_classifier_path = "classifiers_output/video"
        self.stages_log_file_name = "eventsModule.log"
        self.survey_file_name = "survey_results.csv"
        self.audio_header = ['filename', 'max_emotion', 'emotion_label', 'AN', \
        'DI', 'FE', 'HA', 'NE', 'SA']
        self.video_header = ['filename', 'max_emotion', 'emotion_label', 'AN', \
        'FE', 'HA', 'SA', 'SU']
        self.survey_header = ["timestamp","1","1a","2","2a","3","3a","4","4a",\
        "5","5a","6","6a","7","v","name","blank","Equal","SoftEqual"]
        self.survey_labels_dict = {
        "R": "HA",
        "ZD": "SU",
        "Z": "AN",
        "ST": "FE",
        "S": "SA",
        "N": "DI",
        'NE': "NE"
        }
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
