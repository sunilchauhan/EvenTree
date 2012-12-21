class EvenTree(object):
    def __init__(self, graph={}):
        self.graph = graph
        self.visited_node = []
        self.total_forest = 0
     
    def calculate_forest(self):
        for k,v in self.graph.items():
            if k not in self.visited_node:
                key1 = k
                key_list = [key1]
                self.visited_node.append(key1)
                new_dict = defaultdict(list)
                count, new_dict = self.total_count(key_list, self.graph, self.visited_node, new_dict)
                #If count is even number, increase number of total_forest
                if count % 2 == 0:
                    self.total_forest += 1 
                    for key,values in new_dict.iteritems():
                        for i in values:
                            if i in new_dict.keys():
                                #If node has odd number of child
                                #It means that EVEN Tree can be created by taking node as parent
                                if len(new_dict[i]) % 2 != 0:
                                    self.total_forest += 1
        return self.total_forest

    '''
    Recursively count total nodes for node in key_list including the key node
    e.g. graph {2: [1], 3: [1], 4: [3], 5: [2], 6: [1], 7: [2], 8: [6], 9: [8], 10: [8]}
    if we take node 2, the count is 3. since, 2 is the parent of 2 nodes 7 and 5.
    
    '''
    def total_count(self, key_list, graph, visited_node, new_dict, count=1):
        if key_list:
            key1 = key_list.pop(0)        
            for key,values in graph.iteritems():
                if key1 == values[0]:
                    #pushing child node in key_list to get nodes originating from it
                    #Since we want to cut the tree from the original key node
                    key_list.append(key)
                    #mark each child node as visited node
                    self.visited_node.append(key)
                    new_dict[values[0]].append(key)
                    count += 1
            #Recursive call to function for each child node
            count, new_dict = self.total_count(key_list, graph, self.visited_node, new_dict, count)
            
        return ( count, new_dict )

class GraphTests(unittest.TestCase):
    def test_graph1(self):
        graph1 = {2: [1], 3: [1], 4: [3], 5: [2], 6: [1], 7: [2], 8: [6], 9: [8], 10: [8]}
        obj1 = EvenTree(graph1)
        self.assertEqual(obj1.calculate_forest(), 2)

    def test_graph2(self):
        graph2 = {2: [1], 3: [1], 4: [3], 5: [2], 6: [5],
                  7: [1], 8: [1], 9: [2], 10: [7], 11: [10],
                  12: [3], 13: [7], 14: [8], 15: [12], 16: [6],
                  17: [6], 18: [10], 19: [1], 20: [8]}
        obj2 = EvenTree(graph2)
        self.assertEqual(obj2.calculate_forest(),4)        

if __name__ == "__main__":
    import unittest
    from collections import defaultdict, Iterable
    import itertools
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    
