import numpy as np
np.random.seed(0)    # to make the random adj_matrix reproducible
from random import choice
from itertools import combinations
import time
import copy

class Graph:
    def __init__(self, nodes_num_per_set):
        self.nodes_num_per_set = nodes_num_per_set
        self.nodes_num = 2 * nodes_num_per_set
        rand_matrix = np.random.randint(0, 10, (self.nodes_num, self.nodes_num))
        self.adj_matrix = (rand_matrix + rand_matrix.T) / 2   # create a symmetric matrix
        self.adj_matrix[range(self.nodes_num), range(self.nodes_num)] = 0
        #　print(self.adj_matrix)
        
        self.cost = 0
        self.nodes = []
        for node_id in range(self.nodes_num):
            node = {}
            node['id'] = node_id
            self.nodes.append(node)

    def init_group(self):
        for node in self.nodes:
            node['set'] = 0 if node['id'] < self.nodes_num_per_set else 1
        
        return self.nodes
    
    def set_group(self, node_group_set):
        self.nodes = node_group_set
        
    def get_set0_nodes(self):
        return [node for node in self.nodes if node['set'] == 0]

    def get_set1_nodes(self):
        return [node for node in self.nodes if node['set'] == 1]

    def get_cost(self):
        self.cost = 0
        for node0 in self.get_set0_nodes():
            for node1 in self.get_set1_nodes():
                self.cost += self.adj_matrix[node0['id']][node1['id']]
        
        return self.cost
        
    def pick_nodes(self, set_id, pick_node_num):
        set_nodes = self.get_set0_nodes() if set_id == 0 else self.get_set1_nodes()
        picked_nodes = list(combinations(set_nodes, pick_node_num))

        return picked_nodes

    def get_delta_costs(self, picked_nodes0, picked_nodes1):
        delta_costs = 0
        nodes0_inner_weight = 0
        nodes0_out_weight = 0
        nodes1_inner_weight = 0
        nodes1_out_weight = 0
        picked_nodes0_ids = [node['id'] for node in picked_nodes0]
        picked_nodes1_ids = [node['id'] for node in picked_nodes1]

        for node in self.get_set0_nodes():
            if not node['id'] in picked_nodes0_ids:
                for p_node in picked_nodes0:
                    nodes0_inner_weight += self.adj_matrix[p_node['id']][node['id']]
        for node in self.get_set1_nodes():
            if not node['id'] in picked_nodes1_ids:
                for p_node in picked_nodes0:
                    nodes1_out_weight += self.adj_matrix[p_node['id']][node['id']]

        for node in self.get_set1_nodes():
            if not node['id'] in picked_nodes1_ids:
                for p_node in picked_nodes1:
                    nodes1_inner_weight += self.adj_matrix[p_node['id']][node['id']]
        for node in self.get_set0_nodes():
            if not node['id'] in picked_nodes0_ids:
                for p_node in picked_nodes1:
                    nodes1_out_weight += self.adj_matrix[p_node['id']][node['id']]

        delta_costs = nodes0_inner_weight + nodes1_inner_weight - nodes0_out_weight - nodes1_out_weight

        return delta_costs
        
    def exchange_picked_nodes(self, picked_nodes0, picked_nodes1):
        # delta_costs = self.get_delta_costs(picked_nodes0, picked_nodes1)

        assert(len(picked_nodes0) == len(picked_nodes1))
        for node in picked_nodes0:
            self.nodes[node['id']]['set'] = 1 - node['set']
        for node in picked_nodes1:
            self.nodes[node['id']]['set'] = 1 - node['set']

        # self.cost += delta_costs
    
    def fake_exchange(self, picked_nodes0, picked_nodes1):
        assert(len(picked_nodes0) == len(picked_nodes1))

        fake_exchanged_nodes = copy.deepcopy(self.nodes)
        for node in picked_nodes0:
            fake_exchanged_nodes[node['id']]['set'] = 1 - node['set']
        for node in picked_nodes1:
            fake_exchanged_nodes[node['id']]['set'] = 1 - node['set']

        return fake_exchanged_nodes