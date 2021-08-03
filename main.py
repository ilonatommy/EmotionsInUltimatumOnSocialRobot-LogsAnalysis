from statistics.dataAnalyser import DataAnalyser
from aiAnalysers.videoAnalyser import VideoAnalyser
from aiAnalysers.vokaturiAudioAnalyser import VakaturiAudioAnalyser

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
        pass
        sys.exit(0)


if __name__ == "__main__":
    main()
