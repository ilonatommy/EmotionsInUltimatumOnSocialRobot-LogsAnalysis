from enums.gameVersionEnum import GameVersionEnum

import pandas as pd


class GameVersionsStatisticalInfoModel:
    def __init__(self):
        # type: -> None:
        self.__version_counter = {
            GameVersionEnum.EMPHATIC: 0,
            GameVersionEnum.EGOISTIC: 0
        }
        self.__success_versions_counter = {
            GameVersionEnum.EMPHATIC: 0,
            GameVersionEnum.EGOISTIC: 0
        }
        self.__all_versions_counter = 0
        self.__all_success_samples = 0
        self.mode = "count"

    def count2percentage(self):
        if self.mode == "count":
            self.mode = "percentage"
            for key, val in self.__version_counter.iteritems():
                self.__version_counter[key] /= float(self.__all_versions_counter)
                self.__version_counter[key] *= 100.0
                try:
                    self.__success_versions_counter[key] /= float(self.__version_counter[key])
                    self.__success_versions_counter[key] *= 100.0
                except:
                    self.__success_versions_counter[key] = 0.0

    def add_version_sample(self, version):
        self.__version_counter[version] += 1
        self.__all_versions_counter += 1

    def add_success_versions_sample(self, version):
        self.__success_versions_counter[version] += 1
        self.__all_success_samples += 1

    def get_accumulated_correct_percentage(self):
        return float(self.__all_success_samples/float(self.__all_versions_counter))

    def get_keys(self):
        return self.__version_counter.keys()

    def get_version_counts(self):
        return self.__version_counter.values()

    def get_success_version_counts(self):
        return self.__success_versions_counter.values()

    def get_dataframe(self):
        data = []
        for key in self.__version_counter.keys():
            data.append([key, self.__version_counter[key], \
                self.__success_versions_counter[key]])
        return pd.DataFrame(data, columns=["version","count","correct count"])
