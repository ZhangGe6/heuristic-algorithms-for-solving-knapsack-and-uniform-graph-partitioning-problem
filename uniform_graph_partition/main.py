from graph import Graph

from simulated_annealing import SimulatedAnnealing
from tabu import TabuSearch
from brute import BruteSearch

def main():
    graph = Graph(nodes_num_per_set=10)
    
    method = ['brute', 'SimulatedAnnealing', 'TabuSearch'][0]
    if method == 'brute':
        runner = BruteSearch(graph)
    elif method == 'SimulatedAnnealing':
        runner = SimulatedAnnealing(graph, max_iterations=2000, temp_max=5, temp_min=0.1**10, cold_ratio=0.999, exchange_node_num=3)
    elif method == 'TabuSearch':
        runner = TabuSearch(graph, tabu_list_len=2, max_iterations=1000, neighbor_search_num=1)
    
    runner.run()



# def main():
#     strategy = '1'
#     max_iter = 200
#     pick_node_num_set = [1, 2, 3]

#     graph = Graph(nodes_num_per_set=5)
#     graph.init_group()
#     cost = graph.get_cost()
#     with open("./results/strategy" + str(strategy) + "_pick_node_num_set" + str(pick_node_num_set) + ".txt", "w") as f:
#         for i in range(max_iter):
#             exchange = False
#             print("==== iter ", i, " ====")
            
#             if strategy == '1' or strategy == '2':
#                 exchange = True
#                 min_delta_costs = float('inf')
#                 for pick_node_num in pick_node_num_set:
#                     for picked_set0_nodes in graph.pick_nodes(set_id=0, pick_node_num=pick_node_num):
#                         for picked_set1_nodes in graph.pick_nodes(set_id=1, pick_node_num=pick_node_num):
#                             delta_costs = graph.get_delta_costs(picked_set0_nodes, picked_set1_nodes)

#                             # print("if exchange {} and {}, we get delta_costs {}".format(picked_set0_nodes, picked_set1_nodes, delta_costs))
#                             if delta_costs < min_delta_costs:
#                                 min_delta_costs = delta_costs
#                                 tmp_picked_set0_nodes, tmp_picked_set1_nodes = picked_set0_nodes, picked_set1_nodes

#                 # strategy 2: If not P(y) < P(x), return false
#                 if strategy == '2':
#                     if not min_delta_costs < 0:
#                         break      
            
#             if strategy == '3' or strategy == '4':
#                 pick_node_num = choice(pick_node_num_set)
#                 tmp_picked_set0_nodes = choice(graph.pick_nodes(set_id=0, pick_node_num=pick_node_num))
#                 tmp_picked_set1_nodes = choice(graph.pick_nodes(set_id=1 ,pick_node_num=pick_node_num))
#                 delta_costs = graph.get_delta_costs(tmp_picked_set0_nodes, tmp_picked_set1_nodes)
#                 # print("if exchange {} and {}, we get delta_cost {}".format(tmp_picked_set0_nodes, tmp_picked_set1_nodes, delta_costs))
#                 if delta_costs < 0:
#                     exchange = True

#                 # strategy 4: If not P(y) < P(x), return false
#                 if strategy == '4':
#                     if not delta_costs < 0:
#                         break
#             if exchange:
#                 # print("before exchanging")
#                 # # print(" set0", graph.get_set0_nodes())
#                 # # print(" set1", graph.get_set1_nodes())
#                 print(" cost", graph.cost)
#                 # # print(" cost", graph.get_cost())

#                 print(" --> exchange", tmp_picked_set0_nodes, tmp_picked_set1_nodes, "delta cost", graph.get_delta_costs(tmp_picked_set0_nodes, tmp_picked_set1_nodes))
#                 graph.exchange_picked_nodes(tmp_picked_set0_nodes, tmp_picked_set1_nodes)
#                 # print("after exchanging")
#                 # # print(" set0", graph.get_set0_nodes())
#                 # # print(" set1", graph.get_set1_nodes())
#                 print(" cost", graph.cost)
#                 # # print(" cost", graph.get_cost())
#                 # print()
            
        
#             f.write(str(i) + " " + str(graph.cost) + "\n")
    
#     f.close()
    
    
                

if __name__ == '__main__':
    main()
