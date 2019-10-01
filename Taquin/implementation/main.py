import time

from Taquin.implementation.state_modele import State
from Taquin.implementation.taquin_viewer import TaquinViewerHTML

def print_recap(history, frontiere):
    print(f"History length: {len(history)}")
    print(f"Frontiere length: {len(frontiere)}")

def search(init, final_values):
    # Element's position is not important so we can
    # use a set to dramatically improve the lookup time.
    history = set()
    # Here we need to use a list because order mater.
    frontiere = [init]

    while frontiere:
        state = frontiere.pop()
        history.add(state)
        # history.append(state)

        if state.final(final_values):
            print_recap(history, frontiere)
            return state

        ops = state.applicable_operators()

        for op in ops:
            new_state = state.apply(op)

            # * In the context of this exercise, `legal()` is useless
            if (new_state not in frontiere) and (new_state not in history):
                frontiere.insert(0, new_state) # breadth first
                # frontiere.append(new_state) # deep first

    print_recap(history, frontiere)
    return None


if __name__ == '__main__':
    EASY = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    MEDIUM = [[0, 1, 2], [7, 4, 3], [5, 8, 6]]
    HARD = [[4, 0, 2], [3, 5, 1], [6, 7, 8]]
    IMPOSSIBLE = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
    FINAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    start = time.time()

    print("Looking for a solution...")
    value = search(State(MEDIUM), FINAL)
    if value is not None:
        path = []
        while value.parent is not None:
            path.insert(0, value)
            value = value.parent
        path.insert(0, value)
        with TaquinViewerHTML('taquin.html') as viewer:
            for i, state in enumerate(path):
                viewer.add_taquin_state(state.values, title=i)
    else:
        print("No solution for this problem.")

    print(f"Execution time: {time.time() - start} seconds")

