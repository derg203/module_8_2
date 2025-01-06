def personal_sum(num):
    result = 0
    incorrect_data = 0
    for i in num:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
                print(f'некорректный тип данных для подсчета суммы - {i}')
    return result, incorrect_data
def calculate_average(num):
    a = 0
    if isinstance(num,int):
        return None
    try:
        sum, mus = personal_sum(num)
        a = sum / (len(num) - mus)
    except ZeroDivisionError:
        return None
    except TypeError:
        return f'В numbers записан некорректный тип данных'
        a = None
    finally:
        return a
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип#
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3#
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция#
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать