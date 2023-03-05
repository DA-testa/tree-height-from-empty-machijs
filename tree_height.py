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
        task_num = input().upper().strip()

    if task_num == 'F':
        task_num = input().strip()
        input_file = f"{task_num}"
        if not os.path.exists(input_file):
            print(f"{input_file} neeksistē")
            return
        with open(input_file, 'r') as f:
            n = int(f.readline())
            parents = np.fromstring(f.readline().strip(), sep=' ', dtype=int)
            if len(parents) != n:
                return
        tree_height = compute_height(n, parents)
        print(tree_height) 


    elif task_num == 'I':
        n = None
        while not isinstance(n, int) or n < 1 or n > 100000:
            try:
                n = int(input().strip())
            except ValueError:
                print("ievadiet skaitli")
        parents_str = input().strip()
        parents = np.fromstring(parents_str, sep=' ', dtype=int)
        if len(parents) != n:
            return
        tree_height = compute_height(n, parents)
        print(tree_height)
    else:
        return


sys.setrecursionlimit(10**9)
threading.stack_size(2**27)
threading.Thread(target=main).start()
