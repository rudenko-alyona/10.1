def circle_area(r: float) -> float:
    """Подсчет площади окружности"""
    number_pi = 3.14
    circle_area = number_pi * r ** 2
    return circle_area


def format_description(r: float, area: float):
    """Форматированный вывод"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float) -> None:
    """Получение информации об окружности"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


if __name__ == '__main__':
    radius = int(input("Enter circle radius (int): "))
    get_info(radius)

