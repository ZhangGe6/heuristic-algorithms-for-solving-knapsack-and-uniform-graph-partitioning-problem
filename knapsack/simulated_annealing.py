import random
import math
import itertools

class SimulatedAnnealing:
    def __init__(self, knapsack, max_iterations, temp_max, temp_min, cold_ratio, neighbor_search_num):
        self.knapsack = knapsack
        self.ProblemSize = self.knapsack.getProblemSize()
        self.MaxIterations = max_iterations
        self.temp = temp_max
        self.temp_min = temp_min
        self.cold_ratio = cold_ratio
        self.neighbor_search_num = neighbor_search_num

    def initSolution(self):
        '''Returns bit-array of length prob_size'''
        solution = []
        for i in range(self.ProblemSize):
            solution.append(random.randint(0,1))
        while self.knapsack.sumWeights(solution) > self.knapsack.maxWeight:
            packed_index = [index for index in range(len(solution)) if solution[index] == 1]
            unpack_index = random.randint(0, len(packed_index)-1)
            solution[packed_index[unpack_index]] = 0
        
        return solution

    def getAllNeighbouringSolutions(self, cur_solution):
        all_neighbor_solutions = []

        for search_num in range(self.neighbor_search_num):
            choose_indexes = list(itertools.combinations(range(self.ProblemSize), search_num + 1))
            for choose_index in choose_indexes:
                neighbor_solution = cur_solution.copy()
                for index in choose_index:
                    neighbor_solution[index] = 1 - neighbor_solution[index]
                if self.knapsack.sumWeights(neighbor_solution) <= self.knapsack.maxWeight:
                    all_neighbor_solutions.append(neighbor_solution)
        
        return all_neighbor_solutions

    def getMonteCarlo(self, abs_delta_E):
        return math.exp(-1 * abs_delta_E / self.temp)

    def coldDownTemperature(self):
        self.temp *= self.cold_ratio

    def run(self):
        # res_file = open("./results/SA_neighbor" + str(self.neighbor_search_num) + ".txt", "w")
        res_file = open("./results/SA_T_0" + str(self.temp) + ".txt", "w")

        cur_solution = self.initSolution()
        # print(self.knapsack.sumWeights(cur_solution))
        for iter in range(self.MaxIterations):
            cur_sum_value = self.knapsack.sumValues(cur_solution)
            all_neighbor_solutions = self.getAllNeighbouringSolutions(cur_solution)
            # print(self.knapsack.sumWeights(cur_solution))
            neighbor_solution = random.choice(all_neighbor_solutions)
            neighbor_sum_value = self.knapsack.sumValues(neighbor_solution)

            if neighbor_sum_value > cur_sum_value:
                cur_solution = neighbor_solution
            else:
                delta_E = neighbor_sum_value - cur_sum_value  # < 0
                accept_prob = self.getMonteCarlo(math.fabs(delta_E))
                if random.uniform(0, 1) < accept_prob:
                    cur_solution = neighbor_solution
            
            print(iter, self.knapsack.sumWeights(cur_solution), self.knapsack.sumValues(cur_solution))
            res_file.write(str(iter) + " " + str(self.knapsack.sumValues(cur_solution)) + "\n")
            
            self.coldDownTemperature()
            if self.temp < self.temp_min:
                break
