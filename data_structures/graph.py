from typing import List, Tuple, Dict, Any

class Graph:
    """
    TODO    Implement   logging functionality.
    TODO    Implement   unit tests.
    """
    def __init__(self, edges: List[Tuple]) -> None:
        self.edges: List[Tuple] = edges
        self.graph_dict: Dict[List] = {}
        for starting_point, finish_point in self.edges:
            if starting_point in self.graph_dict:
                self.graph_dict[starting_point].append(finish_point)
            else: self.graph_dict[starting_point] = [finish_point]
    
    def get_paths(self, starting_point: Any, finishing_point: Any, path: List[Any] = []) -> List[Any]:
        """_summary_

        Parameters
        ----------
        starting_point : Any
            _description_
        finishing_point : Any
            _description_
        path : List[Any], optional
            _description_, by default []

        Returns
        -------
        List[Any]
            _description_
        """
        path = path + [starting_point]
        if starting_point == finishing_point:
            return [path]
        if starting_point not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[starting_point]:
            if node not in path:
                new_paths = self.get_paths(starting_point=node, finishing_point=finishing_point, path=path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self, starting_point: Any, finishing_point: Any, path: List[Any] = []) -> List[Any]:
        """
        Breadth-First Search Algorithm.

        Parameters
        ----------
        starting_point : Any
            _description_
        finishing_point : Any
            _description_
        path : List[Any], optional
            _description_, by default []

        Returns
        -------
        List[Any]
            _description_
        """
        path = path + [starting_point]
        if starting_point == finishing_point:
            return path
        if starting_point not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[starting_point]:
            if node not in path:
                sp = self.get_shortest_path(starting_point=node, finishing_point=finishing_point, path=path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
        

if __name__ == '__main__':
    routes: List[Tuple] = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York City'),
        ('Dubai', 'New York City'),
        ('New York City', 'Toronto'),
    ]
    
    routes_graph: Graph = Graph(edges=routes)
    
    print(routes_graph.get_paths(starting_point='Mumbai', finishing_point='New York City'))
    print(routes_graph.get_shortest_path(starting_point='Paris', finishing_point='New York City'))
    
    destinations: Dict = {
        'Mumbai': ['Paris', 'Dubai'],
        'Paris': ['Dubai', 'New York City'],
        'New York City': ['Toronto'],
    }