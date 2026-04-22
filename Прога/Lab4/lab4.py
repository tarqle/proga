import sys
from io import StringIO

# ============================================
# ЗАДАЧА 2: ДЕКОРАТОР ДЛЯ ПОДАВЛЕНИЯ ВЫВОДА
# ============================================

def suppress_output(func):
    """
    Декоратор для подавления вывода функции на консоль.
    Перехватывает всё, что функция выводит через print, и подавляет его.
    """
    def wrapper(*args, **kwargs):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            sys.stdout = original_stdout
    
    return wrapper


# ============================================
# ЗАДАЧА 1: ЗАМЫКАНИЕ ДЛЯ ОТСЛЕЖИВАНИЯ HP ГЕРОЯ
# ============================================

def create_hero(initial_hp=100):
    """
    Замыкание для отслеживания HP героя.
    HP не может подниматься больше 100 и опускаться ниже 0.
    
    Args:
        initial_hp: начальное количество HP (по умолчанию 100)
    
    Returns:
        функции take_damage, heal и get_hp
    """
    hp = max(0, min(100, initial_hp))
    
    @suppress_output
    def take_damage(amount):
        nonlocal hp
        old_hp = hp
        hp = max(0, hp - amount)
        print(f"[DEBUG] Урон: {amount}, HP было {old_hp}, стало {hp}")
        return hp
    
    @suppress_output
    def heal(amount):
        nonlocal hp
        old_hp = hp
        hp = min(100, hp + amount)
        print(f"[DEBUG] Лечение: {amount}, HP было {old_hp}, стало {hp}")
        return hp
    
    def get_hp():
        return hp
    
    return take_damage, heal, get_hp


# ============================================
# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("ЗАДАЧА 1: ЗАМЫКАНИЕ ДЛЯ ОТСЛЕЖИВАНИЯ HP ГЕРОЯ")
    print("=" * 60)
    
    take_damage, heal, get_hp = create_hero(100)
    
    print(f"\nНачальное HP: {get_hp()}")
    print("\nВыполняем действия (внутренние DEBUG сообщения подавлены):")
    
    hp = take_damage(30)
    print(f"Герой получил 30 урона -> HP: {hp}")
    
    hp = take_damage(50)
    print(f"Герой получил 50 урона -> HP: {hp}")
    
    hp = take_damage(30)
    print(f"Герой получил 30 урона (попытка уйти в минус) -> HP: {hp}")
    
    hp = heal(20)
    print(f"Герой вылечился на 20 -> HP: {hp}")
    
    hp = heal(50)
    print(f"Герой вылечился на 50 -> HP: {hp}")
    
    hp = heal(100)
    print(f"Герой вылечился на 100 (попытка превысить 100) -> HP: {hp}")
    
    print(f"\nФинальное HP: {get_hp()}")
    
    print("\n" + "=" * 60)
    print("ЗАДАЧА 2: ДЕКОРАТОР ДЛЯ ПОДАВЛЕНИЯ ВЫВОДА")
    print("=" * 60)
    
    def test_function():
        print("Это сообщение должно быть подавлено")
        print("И это тоже")
        return "Функция выполнилась"
    
    print("\n--- Без декоратора ---")
    result1 = test_function()
    print(f"Возвращаемое значение: {result1}")
    
    print("\n--- С декоратором ---")
    decorated_func = suppress_output(test_function)
    result2 = decorated_func()
    print(f"Возвращаемое значение: {result2}")
    
    print("\n" + "=" * 60)
    print("ПРОВЕРКА РАБОТЫ ДЕКОРАТОРА В ЗАМЫКАНИИ")
    print("=" * 60)
    print("Выше при работе с героем не было выведено ни одного [DEBUG] сообщения,")
    print("что доказывает успешную работу декоратора suppress_output.")
