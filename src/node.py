from typing import Optional

class Node:
    def __init__(self, key: int) -> None:
        """Inicializa un nodo.

        Args:
            key (int): El valor de la clave del nodo.

        """
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None