from collections import deque
import random
import itertools

class TabuSearch:
    def __init__(self, knapsack, tabu_list_len, max_iterations, neighbor_search_num):
        self.knapsack = knapsack
        self.ProblemSize = self.knapsack.getProblemSize()
        self.MaxIterations = max_iterations
        self.tabu_list_len = tabu_list_len
        self.tabu_list = deque(maxlen=self.tabu_list_len)
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


    def updateMemory(self, solution):
        self.tabu_list.append(solution)

    def run(self):
        # res_file = open("./results/TabuSearch_neighbor" + str(self.neighbor_search_num) + ".txt", "w")
        res_file = open("./results/tabu_list_len" + str(self.tabu_list_len) + ".txt", "w")
        
        cur_solution = self.initSolution()
        # print(self.knapsack.sumWeights(cur_solution))
        self.updateMemory(cur_solution)
        for iter in range(self.MaxIterations):
            cur_solution_value = self.knapsack.sumValues(cur_solution)
            res_file.write(str(iter) + " " + str(cur_solution_value) + "\n")

            all_neighbor_solutions = self.getAllNeighbouringSolutions(cur_solution=cur_solution)
            neighbor_biggest_value = float("-inf")
            for neighbor_solution in all_neighbor_solutions:
                neighbor_value = self.knapsack.sumValues(neighbor_solution)
                if not neighbor_solution in self.tabu_list:
                    if neighbor_value > neighbor_biggest_value:
                        neighbor_biggest_value = neighbor_value
                        best_feasible_neighbor = neighbor_solution.copy()
            
            # print("cur value {}, find biggest neighbor value {}".format(cur_solution_value, neighbor_biggest_value))
            # if neighbor_biggest_value > cur_solution_value:
            cur_solution = best_feasible_neighbor
            self.updateMemory(cur_solution)
