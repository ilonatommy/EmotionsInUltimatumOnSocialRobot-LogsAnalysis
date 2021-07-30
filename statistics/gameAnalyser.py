from config import Config


class GameAnalyser:
    def __init__(self):
        pass

    def get_coherent_emotions_percentage(self, game):
        coherent_emos = 0
        for stage in game.game_stages:
            if(stage.emotion_survey == stage.sensor_filterd_emotion):
                coherent_emos += 1
        return float(coherent_emos/len(game.game_stages))
