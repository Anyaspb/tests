# Наводим порядок: упорядочиваем курсы по продолжительности

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
    course_dict = {"title": course, "mentors": mentor, "duration": duration}
    courses_list.append(course_dict)

# с этого момента начинается выполнение задания 2.
# на входе у вас есть только список курсов courses_list. про исходные данные, на базе которых он был сделан, вы ничего не знаете

# отсортируйте курсы по длительности (ключ "duration"), но при этом сохраните порядковый номер каждого курса из courses_list
# самое простое - создать новый словарь durations_dict с ключом - duration и значением - исходным номером курса в courses_list
# но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря - это список индексов, а не одно значение
durations_dict = {}

# допишите код цикла так, чтобы в нем вы получали id курса. подсказка: помните про функцию enumerate
for id, key in enumerate(courses_list):
    key = courses_list[id]["duration"]  # получите значение из ключа "duration"
    # допишите код ниже, который добавляет в словарь durations_dict по ключу key значения - id
    durations_dict.setdefault(key, [])
    durations_dict[key].append(id)

# отсортируем словарь по ключам. этот код уже готов, ничего менять не нужно
# здесь мы получаем пары ключ-значение в виде кортежа и функция sorted выполняет сортировку по первым значениям кортежа - ключам
durations_dict = dict(sorted(durations_dict.items()))

# выведите курсы, отсортированные по длительности
# допишите код цикла так, чтобы в нем вы получали из durations_dict ключи и значения:
def sorted_list():
    courses_res = []
    for key, ids in durations_dict.items():
    # допишите код, который проходит по всему списку значений и выводит на экран текст вида "название курса - длительность"
        for id in ids:
            tit = courses_list[id]["title"]
            courses_res.append(f'{tit} - {key} месяцев')
    return courses_res


