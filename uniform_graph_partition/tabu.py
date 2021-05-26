from collections import deque
import random
import itertools
import copy

from graph import Graph

class TabuSearch:
    def __init__(self, graph, tabu_list_len, max_iterations, neighbor_search_num):
        self.graph = graph
        # self.ProblemSize = self.knapsack.getProblemSize()
        self.MaxIterations = max_iterations
        self.tabu_list_len = tabu_list_len
        self.tabu_list = deque(maxlen=self.tabu_list_len)
        self.neighbor_search_num = neighbor_search_num
    
    def initSolution(self):        
        solution = self.graph.init_group()

        return solution

    def getAllNeighbouringSolutions(self):
        all_neighbor_solutions = []

        for ex_node_num in range(self.neighbor_search_num):
            all_set0_picked_nodes = self.graph.pick_nodes(set_id=0, pick_node_num=ex_node_num+1)
            all_set1_picked_nodes = self.graph.pick_nodes(set_id=1, pick_node_num=ex_node_num+1)

            # print("exchanging {} nodes".format(ex_node_num+1))
            for set0_picked_nodes in all_set0_picked_nodes:
                for set1_picked_nodes in all_set1_picked_nodes:
                    neighbor = self.graph.fake_exchange(set0_picked_nodes, set1_picked_nodes)

                    all_neighbor_solutions.append(neighbor)
        
        return all_neighbor_solutions

    def updateMemory(self, solution):
        self.tabu_list.append(solution)

    def run(self):
        # res_file = open("./results/tabu_neighbor" + str(self.neighbor_search_num) + ".txt", "w")
        res_file = open("./results/tabu_list_len" + str(self.tabu_list_len) + ".txt", "w")

        cur_solution = self.initSolution()
        # print(self.knapsack.sumWeights(cur_solution))
        self.updateMemory(cur_solution)
        for iter in range(self.MaxIterations):
            cur_solution_cost = self.graph.get_cost()
            res_file.write(str(iter) + " " + str(cur_solution_cost) + "\n")

            all_neighbor_solutions = self.getAllNeighbouringSolutions()
            neighbor_min_value = float("inf")
            for neighbor_solution in all_neighbor_solutions:
                tmp_graph = copy.deepcopy(self.graph)
                tmp_graph.set_group(neighbor_solution)
                neighbor_cost = tmp_graph.get_cost()
                if not neighbor_solution in self.tabu_list:
                    if neighbor_cost < neighbor_min_value:
                        neighbor_min_value = neighbor_cost
                        best_feasible_neighbor = copy.deepcopy(neighbor_solution)
            
            print("cur cost {}, find minimum neighbor value {}".format(cur_solution_cost, neighbor_min_value))
            

            # if neighbor_min_value < cur_solution_cost:
            cur_solution = best_feasible_neighbor
            self.graph.set_group(cur_solution)
            self.updateMemory(cur_solution)

if __name__ == "__main__":
    graph = Graph(nodes_num_per_set=10)
    TS = TabuSearch(graph, tabu_list_len=10, max_iterations=100, neighbor_search_num=1)
    TS.run()
