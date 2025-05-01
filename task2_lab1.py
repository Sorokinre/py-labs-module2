from task1_lab1 import Profile, MoneyStorage, NumericRatio

if __name__ == "__main__":
    # Создаем экземпляры всех классов
    user_profile = Profile("89997778899", 20, "Roman")
    money_storage = MoneyStorage("Roman", 1000)
    numeric_ratio = NumericRatio(8, 10)

    try:
        # Пытаемся изменить имя пользователя с неверным типом данных
        user_profile.rename(10)
    except TypeError as e:
        print(f"Ошибка при изменении имени: {e}")

    try:
        # Пытаемся внести деньги с неверным типом данных
        money_storage.add_money("qwerty")
    except TypeError as e:
        print(f"Ошибка при пополнении счёта: {e}")

    try:
        # Пытаемся умножить дробь на нечисловые значения
        numeric_ratio.product("a", "a")
    except TypeError as e:
        print(f"Ошибка при умножении дробей: {e}")
