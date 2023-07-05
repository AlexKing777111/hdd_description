"""Новая версия класса HddDescriptor."""
from typing import Optional


class HddDescriptor:
    """Класс для описания свойств жёсткого диска."""

    controller: str
    volume: int
    free_space: int
    occupied_space: int

    def __init__(
        self,
        controller: str = "NoName",
        volume: int = 0,
        free_space: int = 0,
        occupied_space: int = 0,
    ):
        self.validate_types(controller, volume, free_space, occupied_space)
        self.validate_values(volume, free_space, occupied_space)
        self.__controller = str(controller)
        self.__volume = int(volume)
        self.__free_space = int(free_space)
        self.__occupied_space = int(occupied_space)

    @property
    def controller(self) -> Optional[str]:
        return self.__controller

    @property
    def volume(self) -> Optional[int]:
        return self.__volume

    @property
    def free_space(self) -> Optional[int]:
        return self.__free_space

    @property
    def occupied_space(self) -> Optional[int]:
        return self.__occupied_space

    @controller.setter
    def controller(self, controller: str) -> None:
        self.validate_types(
            controller, self.volume, self.free_space, self.occupied_space
        )
        self.__controller = controller

    @volume.setter
    def volume(self, volume: int) -> None:
        self.validate_types(
            self.controller, volume, self.free_space, self.occupied_space
        )
        self.validate_values(volume, self.free_space, self.occupied_space)
        if volume >= self.__occupied_space:
            self.__volume = volume
            self.__free_space = self.__volume - self.__occupied_space
        else:
            raise ValueError("Объем не может быть меньше занятого места")
        self.validate_spaces()

    @free_space.setter
    def free_space(self, free_space: int) -> None:
        self.validate_types(
            self.controller, self.volume, free_space, self.occupied_space
        )
        if free_space <= self.__volume:
            self.__free_space = free_space
            self.__occupied_space = self.__volume - self.__free_space
        else:
            raise ValueError(
                "Свободное место не может быть больше объема диска"
            )
        self.validate_values(self.volume, self.free_space, self.occupied_space)
        self.validate_spaces()

    @occupied_space.setter
    def occupied_space(self, occupied_space: int) -> None:
        self.validate_types(
            self.controller, self.volume, self.free_space, occupied_space
        )
        if occupied_space <= self.__volume:
            self.__occupied_space = occupied_space
            self.__free_space = self.__volume - self.__occupied_space
        else:
            raise ValueError("Занятое место не может быть больше объема диска")
        self.validate_values(self.volume, self.free_space, self.occupied_space)
        self.validate_spaces()

    def validate_types(self, controller, volume, free_space, occupied_space):
        """Метод для валидации типа данных."""
        if type(controller) is not str:
            raise ValueError
        if type(volume) not in (int, float):
            raise ValueError
        if type(free_space) not in (int, float):
            raise ValueError
        if type(occupied_space) not in (int, float):
            raise ValueError

    def validate_values(self, volume, free_space, occupied_space):
        """Метод для валидации значений."""
        if volume < 0 or free_space < 0 or occupied_space < 0:
            raise ValueError

    def validate_spaces(self):
        """Метод для валидации взаимного значения объемов."""
        if self.volume != self.free_space + self.occupied_space:
            raise ValueError
