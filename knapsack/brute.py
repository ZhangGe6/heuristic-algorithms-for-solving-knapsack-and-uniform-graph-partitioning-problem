import itertools
from knapsack import Knapsack

class BruteSearch:
    def __init__(self, knapsack):
        self.knapsack = knapsack
        self.ProblemSize = self.knapsack.getProblemSize()

    def run(self):
        init_solution = [0] * self.ProblemSize
        max_value = float("-inf")
        iter_num = 0
        for i in range(self.ProblemSize):
            choose_indexes = list(itertools.combinations(range(self.ProblemSize), i + 1))
            # print(choose_indexes)
            for choose_index in choose_indexes:
                # print(choose_index)
                iter_num += 1
                solution = init_solution.copy()
                for index in choose_index:
                    solution[index] = 1 - solution[index]
                if self.knapsack.sumWeights(solution) <= self.knapsack.maxWeight:
                    value = self.knapsack.sumValues(solution)
                    if value > max_value:
                        max_value = value
        
        print("run for {} iterations (brute), got the max value {}".format(iter_num, max_value))
        # ref_iter_num = sum([len(list(itertools.combinations(range(self.ProblemSize), i))) for i in range(self.ProblemSize + 1)])
        # print("ref total iter num {}".format(ref_iter_num))



if __name__ == "__main__":
    capacity = 750
    weights = [1, 2, 3]
    values = [3, 2, 1]
    # weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 
    #                106, 110, 113, 115, 118, 120]
    # values = [135, 139, 149, 150, 156, 163, 173, 184, 
    #               192, 201, 210, 214, 221, 229, 240]

    knapsack = Knapsack(weights=weights, values=values, maxWeight=capacity)
    BS = BruteSearch(knapsack)
    BS.run()