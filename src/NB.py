from __future__ import division

class NaiveBayes:
    
    """
    A naive Bayesian classifier. The observation vectors can be
    arbitrary iterable objecs with hashable values. The classes should
    also be hashable.
    """

    def __init__(self):
        self.prior = {}  # Frequency of each class
        self.total = {}  # Frequency of each (class, attr, value)-tuple
        self.count = 0   # Number of observations

    def add(self, cls, obs):
        'Adds an observation to the classifier'
        self.prior[cls] = self.prior.get(cls, 0) + 1
        for idx, val in enumerate(obs):
            key = cls, idx, val
            self.total[key] = self.total.get(key, 0) + 1
        self.count += 1

    def discr(self, cls, obs):
        'Bayesian discriminant. Proportional to posterior probability'
        result = self.prior[cls]/self.count
        for idx, val in enumerate(obs):
            freq = self.total.get((cls, idx, val), 0)
            result *= freq/self.prior[cls]
        return result

    def classify(self, obs):
        'Classifies an observation'
        candidates = [(self.discr(c, obs), c) for c in self.prior]
        return max(candidates)[1]
