import re


def find_matches_in_text(text, patterns):
    matches = {}
    for pattern in patterns:
        found = re.findall(pattern, text)
        if found:
            matches[pattern] = found
    return matches


def clean_numbers(numbers):
    cleaned_numbers = []
    for number in numbers:
        # Удаляем ненужные символы
        cleaned = re.sub(r"[^\d]", "", number)  # Оставляем только цифры
        if cleaned:  # Проверяем, что строка не пустая
            cleaned_numbers.append(cleaned)
    return list(set(cleaned_numbers))  # Удаляем дубликаты


# Пример использования
text = ("Мои номера: +7 (999) 123-45-67, 8-800-555-35-35, +1-800-555-5555 доб. 1234., "
        "сегодня утром заходил почтальон, его номер 79242944412, а также Егор 9250124456,"
        "а вчера был вот тот и его номер 86123132131, 0805314798")
patterns = [
    r"(?:\+?\d{1,4}[\s\-.]?)?(?:\(?\d{1,}\)?[\s\-.]?)?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}(?:\s*(?:ext|доб|#|[*])\s*\d{1,})?",  # Основной шаблон
    # r"\+?\d{1,4}[\s\-.]?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}",  # Без скобок, с кодом страны
    # r"\(?\d{1,}\)?[\s\-.]?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}",  # Без кода страны, но с кодом города
    # r"\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}",  # Простой номер без кода страны и города
    # r'\+?\d{1,4}[\s\-.]?\(?\d{1,}\)?[\s\-.]?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}(?:\s*(?:ext|доб|#|[*])\s*\d{1,})?',  # С добавочным номером
    # r'\+?\d{1,4}[\s\-.]?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}',  # Длинные номера
    # r'\(\+?\d{1,4}\)[\s\-.]?\d{1,}[\s\-.]?\d{1,}[\s\-.]?\d{1,}'  # Код страны в скобках
]


matches = find_matches_in_text(text, patterns)
found_arr = []
for patterns, found in matches.items():
    for num in found:
        found_arr.append(num)

clean_found_arr = clean_numbers(found_arr)
print(clean_found_arr)

# if matches:
#     print("Найдены совпадения:")
#     for pattern, found in matches.items():
#         print(f"Шаблон: '{pattern}' -> Найдено: {found}")
# else:
#     print("Совпадений не найдено.")

