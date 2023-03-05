import sys
import threading
import numpy as np
import os

def read_input():
    while True:
        input_option = input()
        if input_option.upper() == 'I':
            n = int(input().strip())
            parents = np.fromstring(input(), sep=' ', dtype=int)
            return n, parents
        elif input_option.upper() == 'F':
            filename = input()
            while 'a' in filename or not os.path.exists(f"tree-height-from-empty-machijs/test/"):
                filename = input()
            with open(f"tree-height-from-empty-machijs/test/", 'r') as f:
                n = int(f.readline())
                parents = np.fromstring(f.readline(), sep=' ', dtype=int)
            return n, parents
        else:
            print()

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
    n, parents = read_input()
    tree_height = compute_height(n, parents)
    print(tree_height)

sys.setrecursionlimit(10**9)
threading.stack_size(2**27)
threading.Thread(target=main).start()
