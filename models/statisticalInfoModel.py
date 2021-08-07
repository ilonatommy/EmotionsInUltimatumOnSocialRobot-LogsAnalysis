class StatisticalInfoModel:
    def __init__(self):
        # type: -> None:
        self.classes_counter = {
            'AN': 0,
            'DI': 0,
            'FE': 0,
            'HA': 0,
            'NE': 0,
            'SA': 0,
            'SU': 0
        }
        self.all_samples_counter = 0

    def __repr__(self):
        return 'AN: {an}, DI: {di}, FE: {fe}, HA: {ha}, NE: {ne}, SA: {sa}, SU: {su}'.format(\
            an=self.classes_counter['AN'], \
            di=self.classes_counter['DI'], \
            fe=self.classes_counter['FE'], \
            ha=self.classes_counter['HA'], \
            ne=self.classes_counter['NE'], \
            sa=self.classes_counter['SA'], \
            su=self.classes_counter['SU']
        )

    def __str__(self):
        return 'AN: {an}, DI: {di}, FE: {fe}, HA: {ha}, NE: {ne}, SA: {sa}, SU: {su}'.format(\
            an=self.classes_counter['AN'], \
            di=self.classes_counter['DI'], \
            fe=self.classes_counter['FE'], \
            ha=self.classes_counter['HA'], \
            ne=self.classes_counter['NE'], \
            sa=self.classes_counter['SA'], \
            su=self.classes_counter['SU']
        )

    def add_class_sample(self, label):
        self.classes_counter[label] += 1
        self.all_samples_counter += 1
        return self

    def count2percentage(self):
        for c in self.classes_counter:
            c /= self.all_samples_counter

    def percentage2count(self):
        for c in self.classes_counter:
            c *= self.all_samples_counter
