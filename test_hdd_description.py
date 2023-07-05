"""Набор unit-тестов для проверки класса HddDescriptor."""
import pytest

from hdd_descriptor import HddDescriptor


def test_create_hdd_descriptor():
    """Проверка создания экземпляра класса HddDescriptor."""
    hdd = HddDescriptor("NewDescriptor", 10, 5, 5)
    assert (
        hdd.controller == "NewDescriptor"
    ), "Ошибка при создании hdd_descriptor"
    assert hdd.volume == 10, "Ошибка при создании hdd_descriptor"
    assert hdd.free_space == 5, "Ошибка при создании hdd_descriptor"
    assert hdd.occupied_space == 5, "Ошибка при создании hdd_descriptor"


def test_set_controller():
    """Проверка изменения названия HddDescriptor."""
    hdd = HddDescriptor()
    hdd.controller = "NewName"
    assert hdd.controller == "NewName", "Ошибка при изменении controller"


def test_set_no_valid_controller():
    """Проверка ошибки при присвоении невалидного названия."""
    hdd = HddDescriptor()
    with pytest.raises(ValueError):
        hdd.controller = 666


def test_set_free_space():
    """Проверка изменения свободного места."""
    hdd = HddDescriptor(volume=10, free_space=5, occupied_space=5)
    hdd.free_space = 7
    assert hdd.free_space == 7, "Ошибка при изменении свободного места"
    assert hdd.occupied_space == 3, "Ошибка при изменении свободного места"
    assert hdd.volume == 10, "Ошибка при изменении свободного места"


def test_set_no_valid_free_space():
    """Проверка валидности при изменении свободного места."""
    hdd = HddDescriptor(volume=10, free_space=10)
    with pytest.raises(ValueError):
        hdd.free_space = -1
    with pytest.raises(ValueError):
        hdd.free_space = "bad"
    with pytest.raises(
        ValueError, match="Свободное место не может быть больше объема диска"
    ):
        hdd.free_space = 15


def test_set_occured_space():
    """Проверка изменения занятого места."""
    hdd = HddDescriptor(volume=10, free_space=5, occupied_space=5)
    hdd.occupied_space = 7
    assert hdd.free_space == 3, "Ошибка при изменении свободного места"
    assert hdd.occupied_space == 7, "Ошибка при изменении свободного места"
    assert hdd.volume == 10, "Ошибка при изменении свободного места"


def test_set_no_valid_occured_space():
    """Проверка валидности при изменении занятого места."""
    hdd = HddDescriptor(volume=10, free_space=10)
    with pytest.raises(ValueError):
        hdd.occupied_space = -1
    with pytest.raises(ValueError):
        hdd.occupied_space = "bad"
    with pytest.raises(
        ValueError, match="Занятое место не может быть больше объема диска"
    ):
        hdd.occupied_space = 15


def test_set_volume():
    """Проверка изменения объема диска."""
    hdd = HddDescriptor()
    hdd.volume = 50
    assert hdd.volume == 50, "Ошибка при изменении volume"
    assert hdd.free_space == 50, "Ошибка при изменении volume"
    assert hdd.occupied_space == 0, "Ошибка при изменении volume"


def test_set_no_valid_volume():
    """Проверка валидности при изменении объема диска."""
    hdd = HddDescriptor(volume=10, free_space=5, occupied_space=5)
    with pytest.raises(ValueError):
        hdd.volume = -1
    with pytest.raises(ValueError):
        hdd.volume = "bad"
    with pytest.raises(
        ValueError, match="Объем не может быть меньше занятого места"
    ):
        hdd.volume = 4
