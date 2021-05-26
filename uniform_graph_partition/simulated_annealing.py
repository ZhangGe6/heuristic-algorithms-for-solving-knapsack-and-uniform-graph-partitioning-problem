import random
import math
import itertools
import copy

from graph import Graph

class SimulatedAnnealing:
    def __init__(self, graph, max_iterations, temp_max, temp_min, cold_ratio, exchange_node_num):
        self.graph = graph
        # self.ProblemSize = self.knapsack.getProblemSize()
        self.MaxIterations = max_iterations
        self.temp = temp_max
        self.temp_min = temp_min
        self.cold_ratio = cold_ratio
        self.exchange_node_num = exchange_node_num

    def initSolution(self):        
        solution = self.graph.init_group()

        return solution
        
    def getAllNeighbouringSolutions(self):
        all_neighbor_solutions = []

        for ex_node_num in range(self.exchange_node_num):
            all_set0_picked_nodes = self.graph.pick_nodes(set_id=0, pick_node_num=ex_node_num+1)
            all_set1_picked_nodes = self.graph.pick_nodes(set_id=1, pick_node_num=ex_node_num+1)

            # print("exchanging {} nodes".format(ex_node_num+1))
            for set0_picked_nodes in all_set0_picked_nodes:
                for set1_picked_nodes in all_set1_picked_nodes:
                    neighbor = self.graph.fake_exchange(set0_picked_nodes, set1_picked_nodes)

                    all_neighbor_solutions.append(neighbor)

        # for search_num in range(self.neighbor_search_num):
        #     choose_indexes = list(itertools.combinations(range(self.ProblemSize), search_num + 1))
        #     for choose_index in choose_indexes:
        #         neighbor_solution = cur_solution.copy()
        #         for index in choose_index:
        #             neighbor_solution[index] = 1 - neighbor_solution[index]
        #         if self.knapsack.sumWeights(neighbor_solution) <= self.knapsack.maxWeight:
        #             all_neighbor_solutions.append(neighbor_solution)
        
        return all_neighbor_solutions

    def getMonteCarlo(self, abs_delta_E):
        return math.exp(-1 * abs_delta_E / self.temp)

    def coldDownTemperature(self):
        self.temp *= self.cold_ratio

    def run(self):
        # res_file = open("./results/SA_neighbor" + str(self.exchange_node_num) + ".txt", "w")
        res_file = open("./results/SA_T0" + str(self.temp) + ".txt", "w")

        cur_solution = self.initSolution()
        print(self.graph.get_cost())
        for iter in range(self.MaxIterations):
            cur_cost = self.graph.get_cost()
            all_neighbor_solutions = self.getAllNeighbouringSolutions()
            
            # print(self.knapsack.sumWeights(cur_solution))
            neighbor_solution = random.choice(all_neighbor_solutions)
            tmp_graph = copy.deepcopy(self.graph)
            tmp_graph.set_group(neighbor_solution)
            neighbor_cost = tmp_graph.get_cost()

            if neighbor_cost < cur_cost:
                cur_solution = neighbor_solution
            else:
                delta_E = neighbor_cost - cur_cost  # > 0
                accept_prob = self.getMonteCarlo(math.fabs(delta_E))
                if random.uniform(0, 1) < accept_prob:
                    cur_solution = neighbor_solution
            
            self.graph.set_group(cur_solution)
            
            print(iter, self.graph.get_cost())
            res_file.write(str(iter) + " " + str(self.graph.get_cost()) + "\n")

            self.coldDownTemperature()
            if self.temp < self.temp_min:
                break
        
        res_file.close()

if __name__ == "__main__":
    graph = Graph(nodes_num_per_set=10)
    # SA = SimulatedAnnealing(graph, max_iterations=2000, temp_max=5, temp_min=0.1**10, cold_ratio=0.999, exchange_node_num=1)
    SA = SimulatedAnnealing(graph, max_iterations=4000, temp_max=20, temp_min=0.1**10, cold_ratio=0.999, exchange_node_num=1)
    SA.run()
