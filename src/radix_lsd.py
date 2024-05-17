from typing import List

class RadixSortLSDHex:
    """Clase estática para implementar Radix Sort LSD(Least Significant Digit)
    """
    @staticmethod
    def radix_sort_lsd_hex(arr: List[str]) -> List[str]:
        """Ordena una lista de cadenas hexadecimales utilizando el algoritmo de ordenación por Radix Sort LSD (Least Significant Digit).

        Args:
            arr (List[str]): La lista de cadenas hexadecimales a ordenar.

        Returns:
            List[str]: La lista ordenada de cadenas hexadecimales.

        """
        normalized_arr = RadixSortLSDHex.normalize_array(arr)
        max_len = RadixSortLSDHex.find_max_length(normalized_arr)

        for digit_index in range(max_len - 1, -1, -1):
            buckets = RadixSortLSDHex.create_buckets()
            buckets = RadixSortLSDHex.fill_buckets(buckets, normalized_arr, digit_index)
            normalized_arr = RadixSortLSDHex.rebuild_array(buckets)
            print(f"Array after sorting by digit {digit_index}: {normalized_arr}\n")

        final_arr = RadixSortLSDHex.remove_leading_zeros(normalized_arr)
        return final_arr

    @staticmethod
    def normalize_array(arr: List[str]) -> List[str]:
        """Normaliza la lista de cadenas eliminando espacios y convirtiendo a mayúsculas.

        Args:
            arr (List[str]): La lista de cadenas a normalizar.

        Returns:
            List[str]: La lista normalizada.

        """
        max_len = max(len(x.replace(" ", "").upper()) for x in arr)
        return [x.replace(" ", "").upper().zfill(max_len) for x in arr]
    


    @staticmethod
    def find_max_length(arr: List[str]) -> int:
        """Encuentra la longitud máxima de las cadenas en la lista.

        Args:
            arr (List[str]): La lista de cadenas.

        Returns:
            int: La longitud máxima de las cadenas en la lista.

        """
        return max(len(num) for num in arr)

    @staticmethod
    def create_buckets() -> dict:
        """Crea un diccionario de buckets inicialmente vacío.

        Returns:
            dict: El diccionario de buckets.

        """
        return {i: [] for i in "0123456789ABCDEF"}

    @staticmethod
    def fill_buckets(buckets: dict, arr: List[str], digit_index: int) -> dict:
        """Llena los buckets con las cadenas correspondientes según el dígito en la posición especificada.

        Args:
            buckets (dict): Los buckets a llenar.
            arr (List[str]): La lista de cadenas.
            digit_index (int): El índice del dígito a considerar.

        Returns:
            dict: Los buckets actualizados.

        """
        for num in arr:
            digit = num[digit_index]
            buckets[digit].append(num)
        return buckets

    @staticmethod
    def rebuild_array(buckets: dict) -> List[str]:
        """Reconstruye la lista de cadenas a partir de los buckets.

        Args:
            buckets (dict): Los buckets que contienen las cadenas agrupadas por dígitos.

        Returns:
            List[str]: La lista reconstruida de cadenas.

        """
        normalized_arr = []
        for digit in "0123456789ABCDEF":
            normalized_arr.extend(buckets[digit])
        return normalized_arr

    @staticmethod
    def remove_leading_zeros(arr: List[str]) -> List[str]:
        """Elimina los ceros a la izquierda de las cadenas.

        Args:
            arr (List[str]): La lista de cadenas.

        Returns:
            List[str]: La lista de cadenas sin ceros a la izquierda.

        """
        return [x.lstrip('0') or '0' for x in arr]

# Ejemplo de uso
arr: List[str] = ["3C1A", "7E21", "87", "374D", "1C", "4EA", "1964", "A98F", "2B4", "527",
     "1BC", "5432", "78C", "6ADB", "27D", "4F BC", "B72", "EDAD", "AF",
     "C85A", "1111", "985E", "D503", "E527", "F AB", "AEAE", "9F C"]
print("Array before sorted: ", arr)
sorted_arr = RadixSortLSDHex.radix_sort_lsd_hex(arr)
print("Array sorted:", sorted_arr)