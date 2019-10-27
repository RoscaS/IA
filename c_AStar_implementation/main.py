from graph.CitiesNetwork import CitiesNetwork


def print_path(start, path, iterations):
    steps = path.get_path(start)
    print(f"Hops: {iterations}")
    print(f"Best path: {len(steps)}\n")
    for step in steps:
        print(step.id)
    print('-' * 50)


graph = CitiesNetwork()
start = graph.get_vertex(graph['Brussels'])
goal = graph.get_vertex(graph['Prague'])

heuristics = [
    graph.set_NullHeuristic,
    graph.set_XHeuristic,
    graph.set_YHeuristic,
    graph.set_AsCrowFliesHeuristic,
    graph.set_ManhatanHeuristic,
]

if __name__ == '__main__':

    # print(graph)

    for heuristic in heuristics:
        heuristic()
        print_path(start, *graph.search(start, goal))
