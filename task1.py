# TODO: описать базовый класс
class Manager:
    """
    Базовый класс для всех менеджеров

    Атрибуты:
        salary (float): зарплата менеджера
        working_schedule (str): график работы менеджера
    """

    def __init__(self, salary: float, working_schedule: str):
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата должна быть числового типа (int или float)")
        if salary <= 0:
            raise ValueError("Зарплата не может быть отрицательной или нулевой")
        self.salary = float(salary)

        if not isinstance(working_schedule, str):
            raise TypeError("График работы должен быть строкой")
        self.working_schedule = working_schedule

    def __str__(self) -> str:
        return f"Зарплата: {self.salary}, График: {self.working_schedule}"

    def __repr__(self) -> str:
        return f"Manager(salary={self.salary}, working_schedule='{self.working_schedule}')"

    def get_monthly_income(self) -> str:
        """
        Возвращает стандартный доход менеджера за месяц

        :return: Строка с информацией о заработке
        """
        return f'Месячный заработок менеджера: {self.salary}'


# TODO: описать дочерний класс
class Person(Manager):
    """
    Класс для представления конкретного менеджера

    Атрибуты:
        salary (float): зарплата
        working_schedule (str): график работы
        name (str): имя менеджера
    """

    def __init__(self, salary: float, working_schedule: str, name: str):
        super().__init__(salary, working_schedule)
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

    def __str__(self) -> str:
        return f"Менеджер {self.name}, Зарплата: {self.salary}, График: {self.working_schedule}"

    def add_bonus(self, bonus_amount: float) -> None:
        """
        Начисляет премию менеджеру

        :param bonus_amount: Размер премии
        :raises TypeError: Если премия не числового типа
        :raises ValueError: Если премия отрицательная
        """
        if not isinstance(bonus_amount, (float, int)):
            raise TypeError("Премия должна быть числом")
        if bonus_amount < 0:
            raise ValueError("Размер премии не может быть отрицательным")
        self.salary += float(bonus_amount)

    def get_monthly_income(self) -> str:
        """
        Возвращает доход конкретного менеджера за месяц

        :return: Строка с персонализированной информацией о заработке
        """
        return f'Месячный заработок менеджера {self.name}: {self.salary}'