from binary_tree import BinaryTree
from typing import List

# Ejemplo de uso
if __name__ == "__main__":
    arr: List[int] = [129, 11, 413, 5, 6]
    print("Array antes de ser ordenado:", arr)
    binary_tree: BinaryTree = BinaryTree()
    sorted_array: List[int] = binary_tree.tree_sort(arr)
    print("Array ordenado usando Tree Sort:", sorted_array)