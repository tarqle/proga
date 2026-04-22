def calculate_yk(k, x):
    """
    Вычисляет y_k по рекуррентным формулам:
    y₀ = 1
    b₀ = 1/(2x)
    bₖ = bₖ₋₁ · x²
    yₖ = bₖ · yₖ₋₁
    
    Args:
        k: индекс (целое неотрицательное число)
        x: значение x (не может быть 0)
    
    Returns:
        значение y_k
    """
    if x == 0:
        raise ValueError("x не может быть равен 0")
    
    # Начальные значения
    y = 1  # y₀
    b = 1 / (2 * x)  # b₀
    
    # Рекуррентные вычисления от 1 до k
    for i in range(1, k + 1):
        b = b * (x ** 2)  # bₖ = bₖ₋₁ · x²
        y = b * y          # yₖ = bₖ · yₖ₋₁
    
    return y


# Альтернативная версия с рекурсией
def calculate_yk_recursive(k, x):
    """
    Рекурсивная версия вычисления y_k.
    """
    if x == 0:
        raise ValueError("x не может быть равен 0")
    
    def compute_b(k):
        if k == 0:
            return 1 / (2 * x)
        return compute_b(k - 1) * (x ** 2)
    
    def compute_y(k):
        if k == 0:
            return 1
        return compute_b(k) * compute_y(k - 1)
    
    return compute_y(k)


# Примеры использования
if __name__ == "__main__":
    # Тестовые примеры
    print("Расчёт y_k для различных k и x:")
    print("-" * 40)
    
    x = 2
    print(f"x = {x}")
    for k in range(4):
        result = calculate_yk(k, x)
        print(f"  y_{k} = {result}")
    
    print()
    x = 3
    print(f"x = {x}")
    for k in range(4):
        result = calculate_yk(k, x)
        print(f"  y_{k} = {result}")
    
    print()
    print("Проверка рекурсивной версии:")
    print(f"calculate_yk(3, 2) = {calculate_yk(3, 2)}")
    print(f"calculate_yk_recursive(3, 2) = {calculate_yk_recursive(3, 2)}")
