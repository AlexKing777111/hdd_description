# Задача. Покрыть unit тестами класс, который описывает свойства жесткого диска.
# При написании тестов надо учитывать физические свойства hdd.
#
# Возможна ли доработка класса, таким образом, чтобы выполнялся контроль присваиваемых значений (по типу, по наличию, по диапазону)?
from typing import Optional


class HddDescriptor:
    """ """

    controller: str
    volume: int
    free_space: int
    occupied_space: int

    def __init__(
        self,
        controller: str = "NoName",
        volume: int = -1,
        free_space: int = -1,
        occupied_space: int = -1,
    ):
        self.__controller = controller
        self.__volume = volume
        self.__free_space = free_space
        self.__occupied_space = occupied_space

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
        self.__controller = controller

    @volume.setter
    def volume(self, volume: int) -> None:
        self.__volume = volume

    @free_space.setter
    def free_space(self, free_space: int) -> None:
        self.__free_space = free_space

    @occupied_space.setter
    def occupied_space(self, occupied_space: int) -> None:
        self.__occupied_space = occupied_space
