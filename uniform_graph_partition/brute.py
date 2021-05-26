
from numpy.lib.utils import _split_line
from graph import Graph
import itertools
import copy
from tqdm import tqdm

class BruteSearch:
    def __init__(self, graph):
        self.graph = graph
    
    def run(self):
        nodes_num_per_set = self.graph.nodes_num_per_set
        total_nodes_num = 2 * nodes_num_per_set
        choose_indexes = list(itertools.combinations(range(total_nodes_num), nodes_num_per_set))
        # print(choose_indexes)
        all_grounp_set = []
        
        # generate all possilble group settings
        for choose_index in tqdm(choose_indexes):
            # print(self.graph.nodes)
            graph_nodes = copy.deepcopy(self.graph.nodes)
            for i, node in enumerate(graph_nodes):
                if graph_nodes[i]['id'] in choose_index:
                    graph_nodes[i]['set'] = 0
                else:
                    graph_nodes[i]['set'] = 1
            # print(graph_nodes)
            all_grounp_set.append(graph_nodes)

        # find the min cost and its group set
        min_cost = float("inf")
        min_cost_group_set = list()
        for group_set in tqdm(all_grounp_set):
            # print(group_set)
            self.graph.set_group(group_set)
            cost = self.graph.get_cost()
            if cost < min_cost:
                min_cost = cost
                min_cost_group_set = group_set

        print("group {} leads to min cost {}".format(min_cost_group_set, min_cost))

            
if __name__ == "__main__":
    graph = Graph(nodes_num_per_set=10)
    BS = BruteSearch(graph)
    BS.run()
