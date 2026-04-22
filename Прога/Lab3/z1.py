def create_n_dim_array_recursive(n, size, original_n=None):
    """
    Создает n-мерный массив с помощью рекурсии.
    
    Args:
        n: текущая глубина вложенности
        size: размер каждого измерения
        original_n: исходное значение n (для правильной маркировки)
    
    Returns:
        n-мерный список с элементами f'level {original_n}'
    """
    if original_n is None:
        original_n = n
    
    if n == 1:
        return [f'level {original_n}' for _ in range(size)]
    else:
        return [create_n_dim_array_recursive(n - 1, size, original_n) for _ in range(size)]


def create_n_dim_array_iterative(n, size):
    """
    Создает n-мерный массив без рекурсии (итеративно).
    
    Args:
        n: количество измерений (глубина вложенности)
        size: размер каждого измерения
    
    Returns:
        n-мерный список с элементами f'level {n}'
    """
    result = f'level {n}'
    for _ in range(n):
        result = [result for _ in range(size)]
    return result


def pretty_print(arr, depth=0):
    """
    Красиво выводит n-мерный массив с отступами.
    
    Args:
        arr: массив для вывода
        depth: текущая глубина вложенности
    """
    indent = "    " * depth
    
    if not isinstance(arr, list):
        print(f"'{arr}'", end="")
    else:
        if depth == 0:
            print("[")
        else:
            print("[")
        
        for i, item in enumerate(arr):
            print(f"{indent}    ", end="")
            pretty_print(item, depth + 1)
            if i < len(arr) - 1:
                print(",")
            else:
                print()
        
        print(f"{indent}]", end="")


def print_n_dim_array(arr):
    """Выводит n-мерный массив в отформатированном виде."""
    pretty_print(arr)
    print()


# Примеры использования
if __name__ == "__main__":
    print("=" * 50)
    print("СПОСОБ 1: РЕКУРСИВНЫЙ")
    print("=" * 50)
    
    print(">>> create_n_dim_array_recursive(2, 3)")
    result1 = create_n_dim_array_recursive(2, 3)
    print_n_dim_array(result1)
    
    print("\n>>> create_n_dim_array_recursive(3, 2)")
    result2 = create_n_dim_array_recursive(3, 2)
    print_n_dim_array(result2)
    
    print("\n" + "=" * 50)
    print("СПОСОБ 2: ИТЕРАТИВНЫЙ")
    print("=" * 50)
    
    print(">>> create_n_dim_array_iterative(2, 3)")
    result3 = create_n_dim_array_iterative(2, 3)
    print_n_dim_array(result3)
    
    print("\n>>> create_n_dim_array_iterative(3, 2)")
    result4 = create_n_dim_array_iterative(3, 2)
    print_n_dim_array(result4)
    
    print("\n" + "=" * 50)
    print("ПРОВЕРКА ЭКВИВАЛЕНТНОСТИ")
    print("=" * 50)
    
    recursive_result = create_n_dim_array_recursive(2, 3)
    iterative_result = create_n_dim_array_iterative(2, 3)
    
    print(f"Рекурсивный результат: {recursive_result}")
    print(f"Итеративный результат: {iterative_result}")
    print(f"Результаты одинаковы: {recursive_result == iterative_result}")
