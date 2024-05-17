# PRÁCTICA 3

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Práctia que implementa un algoritmo de ordenamiento de cada catgoría vista en clase. Los dos primeros ordenan un arreglo 
de números enteros, mientras que que Radix ordena una secuencia de cadenas( String ) de longitud k en hexadecimal.

## Tabla de Contenidos

1. [Instalación](#instalación)
2. [Uso](#uso)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Contribución](#contribución)
5. [Licencia](#licencia)

## Instalación

```bash
git clone https://github.com/erick-rios/Rios-Erick.git
cd Rios-Erick

```

## Uso


```python
from binary_tree import BinaryTree
from typing import List

# Ejemplo de uso
if __name__ == "__main__":
    arr: List[int] = [129, 11, 413, 5, 6]
    print("Array antes de ser ordenado:", arr)
    binary_tree: BinaryTree = BinaryTree()
    sorted_array: List[int] = binary_tree.tree_sort(arr)
    print("Array ordenado usando Tree Sort:", sorted_array)

# Ejemplo de uso del árbol binario
```

## Estructura del Proyecto


- `src/`: Directorio principal que contiene el código fuente.
  - `binary_tree.py`: Implementación del árbol binario.
  - `local_insertion_sort.py`: Implementación del algoritmo de ordenamiento por inserción local.
  - `node.py`: Implementación de la clase Node.
  - `radix_lsd.py`: Implementación del algoritmo de ordenamiento Radix LSD.
  - `tree_sort.py`: Implementación del algoritmo de ordenamiento Tree Sort.
- `__pycache__/`: Directorio generado automáticamente que contiene archivos compilados.
- `README.md`: Documentación del proyecto (¡este archivo!).

