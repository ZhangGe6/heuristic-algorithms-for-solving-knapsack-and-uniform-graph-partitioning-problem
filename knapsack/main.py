from knapsack import Knapsack
from simulated_annealing import SimulatedAnnealing
from tabu import TabuSearch
from brute import BruteSearch


if __name__ == "__main__":
    capacity = 750
    weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 
                   106, 110, 113, 115, 118, 120]
    values = [135, 139, 149, 150, 156, 163, 173, 184, 
                  192, 201, 210, 214, 221, 229, 240]
    knapsack = Knapsack(weights=weights, values=values, maxWeight=capacity)
    
    method = ['brute', 'SimulatedAnnealing', 'TabuSearch'][0]
    if method == 'brute':
        runner = BruteSearch(knapsack)
    elif method == 'SimulatedAnnealing':
        # runner = SimulatedAnnealing(knapsack, max_iterations=20000, temp_max=500, temp_min=0.1**10, cold_ratio=0.999, neighbor_search_num=2)
        runner = SimulatedAnnealing(knapsack, max_iterations=20000, temp_max=500, temp_min=0.1**10, cold_ratio=0.999, neighbor_search_num=1)
    elif method == 'TabuSearch':
        runner = TabuSearch(knapsack, tabu_list_len=10, max_iterations=100, neighbor_search_num=1)
    
    runner.run()
