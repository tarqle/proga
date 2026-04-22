# Задача 1
alphabet_size = 5  # буквы A, B, C, D, E
length = 5
first_letter_options = 4  # A, B, C, D (не E)
last_letter_options = 4   # B, C, D, E (не A)
middle_options = alphabet_size ** (length - 2)  # 3 позиции по 5 вариантов

total = first_letter_options * middle_options * last_letter_options
print("1. Количество кодовых слов:", total)



# Задача 2: Вычисление количества единиц в двоичной записи числа 4^511 + 2^511 - 511

# Возводим в степень и вычисляем выражение
value = 4**511 + 2**511 - 511

# Переводим в двоичную строку (без префикса '0b')
binary_str = bin(value)[2:]

# Считаем количество единиц
ones_count = binary_str.count('1')

print("2. Количество единиц:", ones_count)



# Задача 3
def smallest_divisors(n):
    """Возвращает список 5 наименьших делителей n, не считая 1"""
    divs = []
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            if d not in divs:
                divs.append(d)
            other = n // d
            if other != d and other not in divs:
                divs.append(other)
        if len(divs) >= 10:  # нам нужно всего 5, но для порядка
            break
    divs.sort()
    return divs[:5]

def M(n):
    divs = smallest_divisors(n)
    if len(divs) < 5:
        return 0
    product = 1
    for d in divs:
        product *= d
    return product

# Ищем 5 наименьших N > 200_000_000, для которых 0 < M(N) < N
start = 200_000_001
found = []
n = start
while len(found) < 5:
    m_val = M(n)
    if 0 < m_val < n:
        found.append((n, m_val))
    n += 1
    if n % 1_000_000 == 0:
        print(f"Проверено до {n}, найдено {len(found)} чисел")

print("\n3. Найденные пары (N, M(N)):")
for n, m_val in found:
    print(f"N = {n}, M(N) = {m_val}")

print("\nЗначения M(N) в порядке возрастания N:")
print([m_val for _, m_val in found])
