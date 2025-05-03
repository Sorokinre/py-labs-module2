# TODO: описать базовый класс
class Employee:
    """
    Базовый класс для всех сотрудников

    Атрибуты:
        base_salary (float): базовая зарплата сотрудника
        position (str): должность сотрудника
    """

    def __init__(self, base_salary: float, position: str):
        if not isinstance(base_salary, (int, float)):
            raise TypeError("Базовая зарплата должна быть числом (int или float)")
        if base_salary <= 0:
            raise ValueError("Базовая зарплата должна быть положительной")
        self.base_salary = float(base_salary)

        if not isinstance(position, str):
            raise TypeError("Должность должна быть строкой")
        self.position = position

    def __str__(self) -> str:
        return f"Зарплата: {self.base_salary}, Должность: {self.position}"

    def __repr__(self) -> str:
        return f"Employee(base_salary={self.base_salary}, position='{self.position}')"

    def get_annual_income(self) -> str:
        """
        Возвращает годовой доход сотрудника

        :return: Строка с информацией о годовом доходе
        """
        return f'Годовой доход сотрудника: {self.base_salary * 12}'


# TODO: описать дочерний класс
class Staff(Employee):
    """
    Класс для представления конкретного сотрудника

    Атрибуты:
        base_salary (float): базовая зарплата
        position (str): должность
        full_name (str): полное имя сотрудника
    """

    def __init__(self, base_salary: float, position: str, full_name: str):
        super().__init__(base_salary, position)
        if not isinstance(full_name, str):
            raise TypeError("Имя должно быть строкой")
        self.full_name = full_name

    def __str__(self) -> str:
        return f"Сотрудник {self.full_name}, Зарплата: {self.base_salary}, Должность: {self.position}"

    def add_bonus(self, bonus_amount: float) -> None:
        """
        Начисляет бонус сотруднику

        :param bonus_amount: Размер бонуса
        :raises TypeError: Если бонус не числового типа
        :raises ValueError: Если бонус отрицательный
        """
        if not isinstance(bonus_amount, (float, int)):
            raise TypeError("Бонус должен быть числом")
        if bonus_amount < 0:
            raise ValueError("Размер бонуса не может быть отрицательным")

        self.base_salary += float(bonus_amount)
