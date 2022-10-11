from Coordinate import Coordinate
from Menu import Menu


def test_menu_cordinate_valid():
    # Arrange / Setup
    coordinateX = 0
    coordinateY = 0
    coordinates = Coordinate(coordinateX, coordinateY)
    validacao = Menu(coordinates)

    # Act / Action
    result = quadrant.get__menu_cordinate_valid()

    # Assert
    assert result == "False"