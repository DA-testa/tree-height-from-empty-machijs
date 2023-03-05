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
    task_num = input()
    if not task_num.isdigit():
        print("nav skaitlis")
        return
    input_file = f"{task_num}.txt"
    if not os.path.exists(input_file):
        print(f"fails {input_file} neeksistē")
        return
    with open(input_file, 'r') as f:
        n = int(f.readline())
        parents = np.fromstring(f.readline(), sep=' ', dtype=int)
    tree_height = compute_height(n, parents)
    print(tree_height)


sys.setrecursionlimit(10**9)
threading.stack_size(2**27)
threading.Thread(target=main).start()
