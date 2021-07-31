from statistics.dataAnalyser import DataAnalyser
from aiAnalysers.videoAnalyser import VideoAnalyser


def main():
    da = DataAnalyser()
    survey_success_rate = da.run_logs_analysis()
    print(survey_success_rate)


if __name__ == "__main__":
    main()
