import time

from implementation.state_modele import State
from implementation.taquin_viewer import TaquinViewerHTML

EASY = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
MEDIUM = [[0, 1, 2], [7, 4, 3], [5, 8, 6]]
HARD = [[4, 0, 2], [3, 5, 1], [6, 7, 8]]
IMPOSSIBLE = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
FINAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def print_recap(history, frontiere):
    print(f"Iterations: {len(history)}")
    print(f"Frontiere length: {len(frontiere)}")


def build_html(value):
    path = []
    while value.parent is not None:
        path.insert(0, value)
        value = value.parent
    path.insert(0, value)
    with TaquinViewerHTML('taquin.html') as viewer:
        for i, state in enumerate(path):
            viewer.add_taquin_state(state.values, title=i)


def search(init, final_values):
    # Element's position is not important so we can
    # use a set to dramatically improve the lookup time.
    history = set()
    # Here we need to use a list because order mater.
    frontiere = [init]

    while frontiere:
        state = frontiere.pop()
        history.add(state)

        if state.final(final_values):
            print_recap(history, frontiere)
            return state

        for op in state.applicable_operators():
            new_state = state.apply(op)

            # * In the context of this exercise, `legal()` is useless
            if (new_state not in frontiere) and (new_state not in history):
                frontiere.insert(0, new_state)  # breadth first
                # frontiere.append(new_state) # depth first

    print_recap(history, frontiere)
    return None


if __name__ == '__main__':
    print("Looking for a solution...")
    start = time.time()
    solution = search(State(MEDIUM), FINAL)
    print(f"Execution time: {time.time() - start} seconds")

    if solution is not None:
        build_html(solution)
    else:
        print("No solution for this problem.")
