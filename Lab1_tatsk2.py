from task_1 import Cat, Student, Prepod  # Импорт классов из task_1

# Создание экземпляров классов
cat1 = Cat("Barsik", 5, "Maine Coon")
student1 = Student("Sidorov", 3, True)
prepod1 = Prepod("Zelikman", 18635)

if __name__ == "__main__":
    try:
        # Попытка вызвать метод add_data с некорректными аргументами для Cat
        cat1.add_data("Invalid", -1, "Invalid")
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        # Попытка вызвать метод add_data с некорректными аргументами для Student
        student1.add_data("Invalid", False, 5)
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        # Попытка вызвать метод add_data с некорректными аргументами для Prepod
        prepod1.add_data("Invalid", -1)
    except ValueError:
        print("Ошибка: неправильные данные")