"""Main Entry Point"""
from MC_Problem import MissionariesAndCannibals
from tree_search import breadth_first_tree_search


def print_path(path):
    for node in path:
        print(node.state.value)

def main():
    problem = MissionariesAndCannibals()
    result = breadth_first_tree_search(problem)
    print_path(result.path())


if __name__ == '__main__':
    main()
