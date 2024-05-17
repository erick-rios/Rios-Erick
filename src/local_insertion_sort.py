from typing import List

class LocalInsertionSort:
    def __init__(self, array: List[int]) -> None:
        """Inicializa una instancia de LocalInsertionSort.

        Args:
            array (List[int]): La lista de enteros que se ordenará localmente.
        
        """
        self.array: List[int] = array

    def sort(self) -> None:
        """Ordena el array utilizando el algoritmo Local Insertion Sort.
        """
        for i in range(1, len(self.array)):
            key: int = self.array[i]
            j: int = i - 1
            while j >= 0 and self.array[j] > key:
                print("Array: ", self.array)
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    def display(self) -> None:
        """Muestra el array ordenado.
        """
        print("Array ordenado usando Local Insertion Sort:")
        for element in self.array:
            print(element, end=" ")
        print()

# Ejemplo de uso
if __name__ == "__main__":
    arr: List[int] = [13, 113, 513, 57, 6]
    print("Array before being sorted: ", arr)
    local_insertion_sort: LocalInsertionSort = LocalInsertionSort(arr)
    local_insertion_sort.sort()
    local_insertion_sort.display()