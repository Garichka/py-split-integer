import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts",
    [
        (10, 3),
        (16, 4),
        (17, 5),
        (3, 4),
        (0, 5),
        (100, 1),
    ]
)
def test_split_integer_basic_constraints(value: int, parts: int) -> None:
    result = split_integer(value, parts)

    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = 4
    result = split_integer(16, parts)

    assert all(part == 4 for part in result)


def test_uneven_split_distribution_logic() -> None:
    value, parts = 10, 3
    result = split_integer(value, parts)

    # Різниця між максимумом і мінімумом не більше 1
    assert max(result) - min(result) <= 1
    # Кількість "більших" елементів має дорівнювати залишку від ділення
    assert result.count(max(result)) == value % parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)

    assert result == [8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)

    assert len(result) == parts
    assert result.count(0) == parts - value
    assert result == sorted(result)


def test_different_number_of_parts_produce_different_lengths() -> None:
    result_3 = split_integer(10, 3)
    result_4 = split_integer(10, 4)

    assert len(result_3) == 3
    assert len(result_4) == 4
    assert result_3 != result_4
