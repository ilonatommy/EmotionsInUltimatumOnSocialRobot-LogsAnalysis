from statisticalAnalysers.dataAnalyser import DataAnalyser
from aiAnalysers.videoAnalyser import VideoAnalyser
from aiAnalysers.vokaturiAudioAnalyser import VakaturiAudioAnalyser
from aiAnalysers.merVideoAnalyser import MERVideoAnalyser

import sys


def main(mode="analysis"):
    if mode == "analysis":
        da = DataAnalyser()
        survey_success_rate = da.run_logs_analysis()
        sys.exit(0)
    if mode == "audio_reanalysis":
        vaa = VakaturiAudioAnalyser()
        vaa.analyse_audio_logs()
        sys.exit(0)
    if mode == "video_reanalysis":
        merva = MERVideoAnalyser()
        merva.analyse_video_logs()
        sys.exit(0)


if __name__ == "__main__":
    main()
