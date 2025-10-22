def total_salary(path) -> tuple:
    total = 0
    average = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines =[el.strip() for el in file.readlines()]
            count_emp = len(lines)

            for line in lines:
                try:
                    name, salary = line.split(",")
                    total += float(salary)
                except ValueError:
                    print(f"Некоректний формат рядка: '{line}'. Пропускаємо цей рядок.")
                    count_emp -= 1
                    continue

            if count_emp == 0:
                print("Помилка: Файл порожній, неможливо розрахувати середнє.")
                return (0, 0)

            average = total / count_emp
            return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return (0, 0)