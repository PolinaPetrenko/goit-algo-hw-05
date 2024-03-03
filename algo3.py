import timeit

# Функція для реалізації алгоритму пошуку підрядка Боєра-Мура
def boyer_moore(text, pattern):
    # Реалізація алгоритму Боєра-Мура
    pass

# Функція для реалізації алгоритму пошуку підрядка Кнута-Морріса-Пратта
def kmp(text, pattern):
    # Реалізація алгоритму Кнута-Морріса-Пратта
    pass

# Функція для реалізації алгоритму пошуку підрядка Рабіна-Карпа
def rabin_karp(text, pattern):
    # Реалізація алгоритму Рабіна-Карпа
    pass

# Завантаження текстових файлів
with open("стаття 1.txt", "r") as file1, open("стаття 2.txt", "r") as file2:
    text1 = file1.read()
    text2 = file2.read()

# Генерація випадкових підрядків
# Ви можете замінити ці рядки на ваші власні підрядки
pattern1_existing = "підрядок1"
pattern1_nonexisting = "вигаданийпідрядок1"
pattern2_existing = "підрядок2"
pattern2_nonexisting = "вигаданийпідрядок2"

# Вимірювання часу для кожного алгоритму та підрядка
for algorithm in [boyer_moore, kmp, rabin_karp]:
    for pattern in [pattern1_existing, pattern1_nonexisting, pattern2_existing, pattern2_nonexisting]:
        time_taken = timeit.timeit(lambda: algorithm(text1, pattern), number=10)  # Вимірюємо час 10 викликів
        print(f"Час виконання {algorithm.__name__} для підрядка '{pattern}' у тексті 1: {time_taken} секунд")
