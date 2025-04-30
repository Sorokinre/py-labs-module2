import re
import doctest


# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Profile:
    def __init__(self, mobile: str, years: int, username: str):
        """
        Конструктор цифрового профиля

        :param mobile: Контактный номер
        :param years: Количество лет
        :param username: Уникальное имя

        Пример:
        >>> account = Profile("89997778899", 30, "Ivan")
        """
        phone_validator = re.compile(r'(8|\+7)\d{10}')
        if not re.fullmatch(phone_validator, mobile):
            raise ValueError('Неверный телефонный номер')
        self.mobile = mobile

        if not isinstance(years, int):
            raise TypeError("Требуется целое число для возраста")
        if years <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.years = years

        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not username.strip():
            raise ValueError("Необходимо указать имя пользователя")
        self.username = username

    def display(self) -> str:
        """
        Отображение профильной информации

        :return: Форматированная строка данных

        Пример:
        >>> account = Profile("89997778899", 30, "Ivan")
        >>> account.display()
        'Профиль: Ivan, Телефон: 89997778899, Возраст: 30'
        """
        return (f'Профиль: {self.username}, '
                f'Телефон: {self.mobile}, '
                f'Возраст: {self.years}')

    def rename(self, new_username: str = 'default') -> None:
        """
        Изменение имени пользователя

        :param new_username: Новый псевдоним (по умолчанию 'default')

        Пример:
        >>> account = Profile("89997778899", 30, "Ivan")
        >>> account.rename("NewIvan")
        """
        if not isinstance(new_username, str):
            raise TypeError("Имя должно быть строковым значением")
        self.username = new_username


# TODO: описать ещё класс
class MoneyStorage:
    def __init__(self, holder: str, funds: float):
        """
        Инициализация денежного хранилища

        :param holder: Владелец средств
        :param funds: Доступные средства

        Пример:
        >>> wallet = MoneyStorage("Ivan", 5000)
        """
        if not isinstance(holder, str):
            raise TypeError("Имя владельца должно быть строкой")
        self.holder = holder

        if not isinstance(funds, (int, float)):
            raise TypeError("Сумма должна быть числовой")
        if funds < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.funds = funds

    def balance(self) -> str:
        """
        Проверка состояния счета

        :return: Информация о средствах

        Пример:
        >>> wallet = MoneyStorage("Ivan", 5000)
        >>> wallet.balance()
        'Владелец: Ivan, Доступно: 5000.00'
        """
        return f'Владелец: {self.holder}, Доступно: {self.funds:.2f}'

    def add_money(self, amount: float = 100.0) -> None:
        """
        Пополнение баланса

        :param amount: Сумма для зачисления

        Пример:
        >>> wallet = MoneyStorage("Ivan", 5000)
        >>> wallet.add_money(1000)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Необходимо указать числовое значение")
        if amount < 100:
            raise ValueError("Минимальный взнос - 100 единиц")
        self.funds += amount

    def take_money(self, amount: float = 100.0) -> None:
        """
        Снятие денежных средств

        :param amount: Запрашиваемая сумма

        Пример:
        >>> wallet = MoneyStorage("Ivan", 5000)
        >>> wallet.take_money(2000)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Необходимо указать числовое значение")
        if amount > self.funds:
            raise ValueError("Недостаточно средств для операции")
        if amount < 100:
            raise ValueError("Минимальная сумма снятия - 100 единиц")
        self.funds -= amount


# TODO: и ещё один
class NumericRatio:
    def __init__(self, top: int, bottom: int):
        """
        Создание дробного соотношения

        :param top: Верхнее значение
        :param bottom: Нижнее значение

        Пример:
        >>> ratio = NumericRatio(5, 8)
        """
        if not isinstance(top, int):
            raise TypeError("Верхнее значение должно быть целым числом")
        self.top = top

        if not isinstance(bottom, int):
            raise TypeError("Нижнее значение должно быть целым числом")
        if bottom == 0:
            raise ValueError("Нижнее значение не может быть нулем")
        self.bottom = bottom

    def as_decimal(self) -> float:
        """
        Преобразование в десятичный формат

        :return: Десятичное представление

        Пример:
        >>> ratio = NumericRatio(5, 8)
        >>> ratio.as_decimal()
        0.625
        """
        return self.top / self.bottom

    def product(self, other_top: int = 1, other_bottom: int = 1) -> str:
        """
        Расчет произведения дробей

        :param other_top: Верхнее значение второй дроби
        :param other_bottom: Нижнее значение второй дроби

        :return: Результат умножения

        Пример:
        >>> ratio = NumericRatio(5, 8)
        >>> ratio.product(3, 4)
        '15/32'
        """
        if not isinstance(other_top, int):
            raise TypeError("Верхнее значение должно быть целым числом")

        if not isinstance(other_bottom, int):
            raise TypeError("Нижнее значение должно быть целым числом")
        if other_bottom == 0:
            raise ValueError("Нижнее значение не может быть нулем")

        result_top = self.top * other_top
        result_bottom = self.bottom * other_bottom
        return f'{result_top}/{result_bottom}'


if __name__ == "__main__":
    doctest.testmod()
