from typing import List, Any, Dict

from data.exract_data import extract_lines
from graph.SearchableGraph import SearchableGraph
from containers.City import City

POSITIONS = 'data/positions.txt'
EDGES = 'data/connections.txt'

raw_data = {
    'cities': extract_lines(POSITIONS),
    'edges': extract_lines(EDGES)
}


class CitiesNetwork(SearchableGraph):
    def __init__(self):
        super().__init__()
        self.cities: Dict[str, City] = self._create_cities()
        self._init_graph()
        self._create_edges()

    def __str__(self):
        return '\n'.join(str(i) for i in self)

    def __getitem__(self, name):
        return self.cities[name]

    def _create_cities(self) -> Dict[str, City]:
        cities = [City(*i.split(' ')) for i in raw_data['cities']]
        return {i.name: i for i in cities}

    def _create_edges(self) -> None:
        for args in [i.split(' ') for i in raw_data['edges']]:
            self.add_edge(self.cities[args[0]], self.cities[args[1]], args[2])

    def _init_graph(self):
        for node in self.cities.values():
            self.add_vertex(node)
