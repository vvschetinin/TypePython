"""Базовые тесты для TypePython."""

from pathlib import Path

from main import NumberStats, compute_stats, load_numbers


def test_compute_stats_empty() -> None:
    result = compute_stats([])
    assert result == NumberStats(count=0, total=0.0, average=0.0)


def test_compute_stats_normal() -> None:
    result = compute_stats([10.0, 20.0, 30.0])
    assert result.count == 3
    assert result.total == 60.0
    assert result.average == 20.0


def test_load_numbers(tmp_path: Path) -> None:
    file = tmp_path / "nums.txt"
    file.write_text("1.5\n2.5\n3\n", encoding="utf-8")
    numbers = load_numbers(file)
    assert numbers == [1.5, 2.5, 3.0]
