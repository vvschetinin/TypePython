"""Простой пример: обработка списка чисел с type hints (Python 3.14)."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class NumberStats:
    """Статистика по списку чисел."""

    count: int
    total: float
    average: float


def compute_stats(numbers: list[float]) -> NumberStats:
    """Вычисляет количество, сумму и среднее."""
    if not numbers:
        return NumberStats(count=0, total=0.0, average=0.0)

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return NumberStats(count=count, total=total, average=average)


def load_numbers(path: Path) -> list[float]:
    """Читает числа из текстового файла (по одному на строку)."""
    text = path.read_text(encoding="utf-8")
    return [float(line.strip()) for line in text.splitlines() if line.strip()]


def main() -> None:
    """Точка входа."""
    data_file = Path("data.txt")

    # Создаём демо-файл, если его нет
    if not data_file.exists():
        data_file.write_text("10\n20.5\n30\n15.5\n", encoding="utf-8")

    numbers = load_numbers(data_file)
    stats = compute_stats(numbers)

    print(f"Файл: {data_file}")
    print(f"Количество: {stats.count}")
    print(f"Сумма: {stats.total:.2f}")
    print(f"Среднее: {stats.average:.2f}")


if __name__ == "__main__":
    main()
