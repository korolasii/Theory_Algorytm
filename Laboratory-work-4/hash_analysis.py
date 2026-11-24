M_DIV = 13
M_MUL = 16
A = 0.6180339887
DELETED = "DELETED"

TEXT = "Людина без друзів — як дерево без коріння"
ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
LETTER_POSITIONS = {letter: i + 1 for i, letter in enumerate(ALPHABET)}


def get_words(text):
    words = []
    for word in text.lower().replace("—", " ").split():
        if word not in words:
            words.append(word)
    return words


def get_key(word):
    return sum(LETTER_POSITIONS[char] for char in word)


def hash_division(word):
    return get_key(word) % M_DIV


def hash_multiplication(word):
    return int(M_MUL * (get_key(word) * A % 1))


# ---------- Хешування з ланцюжками ----------
def chain_build(words, m, h):
    table = [[] for _ in range(m)]
    for word in words:
        table[h(word)].append(word)
    return table


def chain_search(table, word, h):
    comparisons = 0
    for item in table[h(word)]:
        comparisons += 1
        if item == word:
            return True, comparisons
    return False, comparisons


def chain_delete(table, word, h):
    found, comparisons = chain_search(table, word, h)
    if found:
        table[h(word)].remove(word)
    return found, comparisons


# ---------- Хешування з відкритою адресацією ----------
def open_build(words, m, h):
    table = [None] * m
    for word in words:
        for i in range(m):
            address = (h(word) + i) % m
            if table[address] is None or table[address] == DELETED:
                table[address] = word
                break
    return table


def open_search(table, word, h):
    comparisons = 0
    for i in range(len(table)):
        address = (h(word) + i) % len(table)
        if table[address] is None:
            break
        # Порівняння з ключем (або з міткою DELETED) у зайнятій комірці
        comparisons += 1
        if table[address] == word:
            return address, comparisons
    return -1, comparisons


def open_delete(table, word, h):
    address, comparisons = open_search(table, word, h)
    if address != -1:
        table[address] = DELETED
    return address != -1, comparisons


def analyse(name, words, m, h, build, search, delete):
    print(f"--- {name} (m = {m}) ---")
    total = 0
    worst = 0
    for word in words:
        s = search(build(words, m, h), word, h)[1]
        d = delete(build(words, m, h), word, h)[1]
        print(f"{word}: пошук {s}, видалення {d}")
        total += s
        worst = max(worst, s)
    leaders = [w for w in words if search(build(words, m, h), w, h)[1] == worst]
    print(f"Максимум: {worst} ({', '.join(leaders)})")
    print(f"Середнє: {total}/{len(words)} = {total / len(words):.3f}")


words = get_words(TEXT)
alpha_div = len(words) / M_DIV
alpha_mul = len(words) / M_MUL

analyse("Ланцюжки, метод ділення", words, M_DIV, hash_division,
        chain_build, chain_search, chain_delete)
analyse("Ланцюжки, метод множення", words, M_MUL, hash_multiplication,
        chain_build, chain_search, chain_delete)
analyse("Відкрита адресація, метод ділення", words, M_DIV, hash_division,
        open_build, open_search, open_delete)
analyse("Відкрита адресація, метод множення", words, M_MUL, hash_multiplication,
        open_build, open_search, open_delete)

print("--- Теоретична оцінка успішного пошуку ---")
for name, alpha in (("ділення", alpha_div), ("множення", alpha_mul)):
    print(f"Метод {name}: alpha = {alpha:.3f}, ланцюжки 1 + alpha/2 = "
          f"{1 + alpha / 2:.3f}, відкрита адресація "
          f"(1 + 1/(1 - alpha))/2 = {(1 + 1 / (1 - alpha)) / 2:.3f}")

print("--- Відкладене видалення (відкрита адресація, метод ділення) ---")
table = open_build(words, M_DIV, hash_division)
open_delete(table, "без", hash_division)
print("Після видалення «без»:", table[6:9])
address, count = open_search(table, "коріння", hash_division)
print(f"Пошук «коріння»: комірка {address}, порівнянь {count}")
