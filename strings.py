from pathlib import Path

def string_length(value: str) -> int:
    """Количество символов Python, включая пробелы и переводы строк."""
    if not isinstance(value, str):
        raise TypeError("Ожидается строка")
    return len(value)

def save_string(value: str, filename: str | Path) -> Path:
    """Сохранить строку в UTF-8; существующий файл перезаписывается."""
    string_length(value)
    path = Path(filename)
    with path.open('w', encoding='utf-8', newline='') as stream:
        stream.write(value)
    return path
