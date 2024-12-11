import string
from collections import Counter


def read_text_file(filename):
    """Читает текст из файла и возвращает его как строку."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def count_total_characters(text):
    """Считает общее количество символов в тексте."""
    return len(text)


def count_letters(text):
    """Считает количество букв в тексте (без пробелов и знаков препинания)."""
    return sum(c.isalpha() for c in text)


def count_total_lines(text):
    """Считает общее количество строк в тексте."""
    return len(text.splitlines())


def count_non_empty_lines(text):
    """Считает количество непустых строк в тексте."""
    return sum(1 for line in text.splitlines() if line.strip())


def count_total_words(text):
    """Считает общее количество слов в тексте."""
    return len(text.split())


def count_words_per_line(text):
    """Возвращает количество слов в каждой строке."""
    return [len(line.split()) for line in text.splitlines()]


def count_characters_per_line(text):
    """Возвращает количество символов в каждой строке."""
    return [len(line) for line in text.splitlines()]


def find_repeated_words(text):
    """Находит повторяющиеся слова в тексте с указанием их количества."""
    words = text.split()
    word_count = Counter(words)
    return {word: count for word, count in word_count.items() if count > 1}


def letter_frequency_analysis(text):
    """Проводит частотный анализ букв в тексте."""
    letters = [c.lower() for c in text if c.isalpha()]
    return Counter(letters)


def find_extra_characters(text):
    """Находит и считает посторонние символы (пробелы и знаки препинания)."""
    extra_chars = Counter(c for c in text if not c.isalnum() and not c.isspace())
    return {char: count for char, count in extra_chars.items()}


def write_results_to_file(results, output_filename):
    """Записывает результаты анализа в файл."""
    with open(output_filename, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')


def main():
    input_filename = 'poem.txt'  # Укажите имя вашего входного файла
    output_filename = 'result.txt'

    # Чтение текста из файла
    text = read_text_file(input_filename)

    # Анализ текста
    results = []
    results.append(f"1. Всего символов в тексте - {count_total_characters(text)}")
    results.append(f"2. Букв в тексте - {count_letters(text)}")
    results.append(f"3. Всего строк в тексте - {count_total_lines(text)}")
    results.append(f"4. Непустых строк в тексте - {count_non_empty_lines(text)}")
    results.append(f"5. Всего слов в тексте - {count_total_words(text)}")

    # Анализ слов по строкам
    words_per_line = count_words_per_line(text)
    results.append("6. Анализ слов по строкам:")
    for i, count in enumerate(words_per_line, start=1):
        results.append(f"{i} строка - {count} слов")

    # Анализ символов по строкам
    characters_per_line = count_characters_per_line(text)
    results.append("7. Анализ символов по строкам:")
    for i, count in enumerate(characters_per_line, start=1):
        results.append(f"{i} строка - {count} символов")

    # Повторяющиеся слова
    repeated_words = find_repeated_words(text)
    results.append("8. Повторяющиеся слова:")
    for word, count in repeated_words.items():
        results.append(f"{word} - {count}")

    # Частотный анализ букв
    letter_freq = letter_frequency_analysis(text)
    results.append("9. Частотный анализ текста:")
    for letter, count in letter_freq.items():
        results.append(f"{letter} - {count}")

    # Прочие символы
    extra_chars = find_extra_characters(text)
    results.append("10. Прочие символы:")
    for char, count in extra_chars.items():
        results.append(f"{char} - {count}")

    # Записываем результаты в файл
    write_results_to_file(results, output_filename)

    print("Анализ текста завершен. Результаты записаны в result.txt.")


if __name__ == "__main__":
    main()