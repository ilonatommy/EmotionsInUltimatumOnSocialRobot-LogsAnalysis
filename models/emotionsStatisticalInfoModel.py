import pandas as pd

class EmotionsStatisticalInfoModel:
    def __init__(self):
        # type: -> None:
        self.__classes_counter = {
            'AN': 0,
            'DI': 0,
            'FE': 0,
            'HA': 0,
            'NE': 0,
            'SA': 0,
            'SU': 0
        }
        self.__correct_samples_counter = {
            'AN': 0,
            'DI': 0,
            'FE': 0,
            'HA': 0,
            'NE': 0,
            'SA': 0,
            'SU': 0
        }
        self.__all_samples_counter = 0
        self.__all_correct_samples = 0
        self.mode = "count"

    def __repr__(self):
        sign = ""
        overall_score = self.__all_correct_samples
        if self.mode == "percentage":
            sign = "%"
            overall_score /= float(self.__all_samples_counter) *0.01

        return 'TOTAL: {overall_score}\nAN: {can}{sign}/{an}{sign}, DI: {cdi}{sign}/{di}{sign}, FE: {cfe}{sign}/{fe}{sign}, HA: {cha}{sign}/{ha}{sign}, NE: {cne}{sign}/{ne}{sign}, SA: {csa}{sign}/{sa}{sign}, SU: {csu}{sign}/{su}{sign}'.format(\
            an=self.__classes_counter['AN'], \
            di=self.__classes_counter['DI'], \
            fe=self.__classes_counter['FE'], \
            ha=self.__classes_counter['HA'], \
            ne=self.__classes_counter['NE'], \
            sa=self.__classes_counter['SA'], \
            su=self.__classes_counter['SU'], \
            can=self.__correct_samples_counter['AN'], \
            cdi=self.__correct_samples_counter['DI'], \
            cfe=self.__correct_samples_counter['FE'], \
            cha=self.__correct_samples_counter['HA'], \
            cne=self.__correct_samples_counter['NE'], \
            csa=self.__correct_samples_counter['SA'], \
            csu=self.__correct_samples_counter['SU'], \
            sign=sign, \
            overall_score=overall_score, \
        )

    def __str__(self):
        sign = ""
        overall_score = self.__all_correct_samples
        if self.mode == "percentage":
            sign = "%"
            overall_score /= float(self.__all_samples_counter) *0.01

        return 'TOTAL: {overall_score}\nAN: {can}{sign}/{an}{sign}, DI: {cdi}{sign}/{di}{sign}, FE: {cfe}{sign}/{fe}{sign}, HA: {cha}{sign}/{ha}{sign}, NE: {cne}{sign}/{ne}{sign}, SA: {csa}{sign}/{sa}{sign}, SU: {csu}{sign}/{su}{sign}'.format(\
            an=self.__classes_counter['AN'], \
            di=self.__classes_counter['DI'], \
            fe=self.__classes_counter['FE'], \
            ha=self.__classes_counter['HA'], \
            ne=self.__classes_counter['NE'], \
            sa=self.__classes_counter['SA'], \
            su=self.__classes_counter['SU'], \
            can=self.__correct_samples_counter['AN'], \
            cdi=self.__correct_samples_counter['DI'], \
            cfe=self.__correct_samples_counter['FE'], \
            cha=self.__correct_samples_counter['HA'], \
            cne=self.__correct_samples_counter['NE'], \
            csa=self.__correct_samples_counter['SA'], \
            csu=self.__correct_samples_counter['SU'], \
            sign=sign, \
            overall_score=overall_score, \
        )

    def count2percentage(self):
        if self.mode == "count":
            self.mode = "percentage"
            for key, val in self.__classes_counter.iteritems():
                self.__classes_counter[key] /= float(self.__all_samples_counter)
                self.__classes_counter[key] *= 100.0
                try:
                    self.__correct_samples_counter[key] /= float(self.__classes_counter[key])
                    self.__correct_samples_counter[key] *= 100.0
                except:
                    self.__correct_samples_counter[key] = 0.0

    def add_class_sample(self, label):
        self.__classes_counter[label] += 1
        self.__all_samples_counter += 1

    def add_correct_class_sample(self, label):
        self.__correct_samples_counter[label] += 1
        self.__all_correct_samples += 1

    def get_accumulated_correct_percentage(self):
        return float(self.__all_correct_samples/float(self.__all_samples_counter))

    def get_keys(self):
        return self.__classes_counter.keys()

    def get_sample_counts(self):
        return self.__classes_counter.values()

    def get_correct_sample_counts(self):
        return self.__correct_samples_counter.values()

    def get_dataframe(self):
        data = []
        for key in self.__classes_counter.keys():
            data.append([key, self.__classes_counter[key], \
                self.__correct_samples_counter[key]])
        return pd.DataFrame(data, columns=["label","count","correct count"])
