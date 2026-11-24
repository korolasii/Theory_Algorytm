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


def build_closed_hash_table(words, m, hash_function):
    table = [None] * m
    for word in words:
        k = get_key(word)
        start = hash_function(k)
        print(f"{word}: k = {k}, h(k) = {start}.", end=" ")
        # Лінійне дослідження: h(k, i) = (h(k) + i) mod m
        for i in range(m):
            address = (start + i) % m
            if table[address] is None:
                table[address] = word
                print(f"Вставляємо в комірку {address}")
                break
            print(f"Комірка {address} зайнята ({table[address]}).", end=" ")
        else:
            print("Помилка: таблиця заповнена")
    return table


def display_hash_table(table):
    print("Індекс | Слово")
    print("-------|-------")
    for i, word in enumerate(table):
        print(f"{i:02d}     | {word if word is not None else '(NULL)'}")


words = get_words(TEXT)
print("Слова:", words)

print(f"--- Метод ділення (m = {M_DIV}) ---")
display_hash_table(build_closed_hash_table(words, M_DIV, hash_division))

print(f"--- Метод множення (m = {M_MUL}) ---")
display_hash_table(build_closed_hash_table(words, M_MUL, hash_multiplication))
