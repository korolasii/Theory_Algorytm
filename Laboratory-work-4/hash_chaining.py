M_DIV = 13
M_MUL = 16
A = 0.6180339887

TEXT = "Людина без друзів — як дерево без коріння"
ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
LETTER_POSITIONS = {letter: i + 1 for i, letter in enumerate(ALPHABET)}


def get_words(text):
    # Словник містить лише унікальні ключі
    words = []
    for word in text.lower().replace("—", " ").split():
        if word not in words:
            words.append(word)
    return words


def get_key(word):
    return sum(LETTER_POSITIONS[char] for char in word)


def hash_division(k):
    return k % M_DIV


def hash_multiplication(k):
    return int(M_MUL * (k * A % 1))


def build_open_hash_table(words, m, hash_function):
    table = [[] for _ in range(m)]
    for word in words:
        k = get_key(word)
        address = hash_function(k)
        if table[address]:
            print(f"{word}: k = {k}, h(k) = {address}. "
                  f"Колізія, додаємо в кінець ланцюжка {table[address]}")
        else:
            print(f"{word}: k = {k}, h(k) = {address}. Комірка порожня, вставляємо")
        table[address].append(word)
    return table


def display_hash_table(table):
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


words = get_words(TEXT)
print("Слова:", words)

print(f"--- Метод ділення (m = {M_DIV}) ---")
display_hash_table(build_open_hash_table(words, M_DIV, hash_division))

print(f"--- Метод множення (m = {M_MUL}) ---")
display_hash_table(build_open_hash_table(words, M_MUL, hash_multiplication))
