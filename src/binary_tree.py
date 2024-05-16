from typing import List, Optional
from node import Node


class BinaryTree:
    """Clase para el uso de estructura de datos Binary Tree
    """
    def __init__(self) -> None:
        """Inicializa un nuevo árbol binario.

        Este método inicializa un nuevo árbol binario con raíz nula.

        """
        self.root: Optional[Node] = None

    def insert(self, key: int) -> None:
        """Inserta un nuevo nodo en el árbol.

        Args:
            key (int): El valor de la clave del nuevo nodo a insertar.

        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: Node, key: int) -> None:
        """Inserta recursivamente un nuevo nodo en el árbol.

        Args:
            node (Node): El nodo actual en el que se está insertando.
            key (int): El valor de la clave del nuevo nodo a insertar.

        """
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def in_order_traversal(self, node: Optional[Node]) -> None:
        """Realiza un recorrido en orden del árbol.

        Args:
            node (Optional[Node]): El nodo a partir del cual comenzar el recorrido.

        """
        if node:
            self.in_order_traversal(node.left)
            print(node.key, end=" ")
            self.in_order_traversal(node.right)

    def tree_sort(self, array: List[int]) -> List[int]:
        """Ordena una lista utilizando un árbol binario.

        Args:
            array (List[int]): La lista de elementos a ordenar.

        Returns:
            List[int]: La lista ordenada.

        """
        for item in array:
            self.insert(item)

        sorted_array: List[int] = []
        self._in_order_traversal_to_list(self.root, sorted_array)
        print("Sorted Array: ", sorted_array)
        return sorted_array

    def _in_order_traversal_to_list(self, node: Optional[Node], sorted_array: List[int]) -> None:
        """Convierte un árbol en una lista ordenada.

        Args:
            node (Optional[Node]): El nodo a partir del cual comenzar el recorrido.
            sorted_array (List[int]): La lista donde se almacenarán los elementos ordenados.

        """
        if node:
            self._in_order_traversal_to_list(node.left, sorted_array)
            sorted_array.append(node.key)
            self._in_order_traversal_to_list(node.right, sorted_array)
            print("_in_order_traversal Array: ", sorted_array)