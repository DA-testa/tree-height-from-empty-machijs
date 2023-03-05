import sys
import threading
import numpy as np
import os

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    root = None

    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    def height(node):
        if not tree[node]:
            return 1
        return 1 + np.max([height(child) for child in tree[node]])

    return height(root)


def main():
    task_num = None
    while task_num not in ['F', 'I']:
        task_num = input().upper()

    if task_num == 'F':
        task_num = input()
        input_file = f"{task_num}"
        if not os.path.exists(input_file):
            print(f"{input_file} neeksistē")
            return
        with open(input_file, 'r') as f:
            n = int(f.readline())
            parents = np.fromstring(f.readline(), sep=' ', dtype=int)
            if len(parents) != n:
                return
        tree_height = compute_height(n, parents)
        print(tree_height) 


    elif task_num == 'I':
        n = None
        while not isinstance(n, int) or n < 1 or n > 100000:
            try:
                n = int(input("Enter number of nodes (1-100000): "))
            except ValueError:
                print("Error: number of nodes must be a positive integer!")
        parents_str = input("Enter parent nodes (space-separated): ")
        parents = np.fromstring(parents_str, sep=' ', dtype=int)
        if len(parents) != n:
            print("Error: invalid number of parent nodes!")
            return
        tree_height = compute_height(n, parents)
        print(tree_height)
    else:
        print("Error: invalid input!")
        return


sys.setrecursionlimit(10**9)
threading.stack_size(2**27)
threading.Thread(target=main).start()
