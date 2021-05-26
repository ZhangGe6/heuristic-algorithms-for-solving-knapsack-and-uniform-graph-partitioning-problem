class Knapsack:
    def __init__(self, weights, values, maxWeight):
        self.weights = weights
        self.values = values
        self.maxWeight = maxWeight

    def getProblemSize(self):
        return len(self.values)

    def sumWeights(self, solution):
        w = 0
        for i in range(len(solution)):
            w += solution[i] * self.weights[i]
        return w

    def sumValues(self, solution):
        v = 0
        for i in range(len(solution)):
            v += solution[i] * self.values[i]
        return v