# Это вы мне? Подсчитываем тёзок на каждом курсе

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

# с этого момента начинается выполнение задания 4.
# на входе у вас есть только список курсов courses_list. про исходные данные, на базе которых он был сделан, вы ничего не знаете

# на каждом курсе в отдельности вам нужно 1) найти имена, которые встречаются более 1 раза, и
# 2) отобрать людей (Имя + Фамилия), для моторых совпало Имя. это и будут наши тёзки

def dublicate_names():
	dublicate_names_result = []
	for course in courses_list:
		mentors_list = []
		# самостоятельно напишите код, который создает множество уникальных имен без фамилий
		# Подсказка: вам нужно вспомнить и повторить код из Задания 1 по Множествам
		# результат (уникальные имена без фамилий) запишите в переменную под названием unique_names, преобразуйте в список и отсортируйте по возрастанию
		# это нужно, чтобы ваша программа всегда давала один и тот же результат и тренажер смог его сверить
		for mentor in course["mentors"]:
			mentors_list.append(mentor.split(' ')[0])
			unique_names = sorted(set(mentors_list))

		# сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код

		# теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
		# допишите код ниже

		# напишите алгоритм, который подсчитывает частоту встречаемости каждого имени из names_set в исходном списке преподавателей
		# Подсказка: при работе со строками воспользуйтесь конструкцией in
		# Внимание: в список same_name_list вы будете сохранять найденных тёзок-преподавателей
		same_name_list = []
		# организуйте цикл по всем именам на курсе из множества:
		for name in unique_names:
			# подсчитайте частоту встречаемости имени (должно быть более 1 раза):
			if mentors_list.count(name) > 1:
				# сделайте цикл по исходному списку преподавателей (с Именем и Фамилией)
				for mentor in course["mentors"]:
					# найдите тех преподавателей, у кого совпало имя (для них if вернет True)
					if name in mentor:
						# добавьте преподавателя с этим именем в список тёзок
						same_name_list.append(mentor)
		# если список тёзок не пустой, выведите всех преподавателей из него


		if same_name_list != []:
			# дополните конструкцию ниже, чтобы выводилось сообщение такого вида: На курсе Название есть тёзки: тёзки через запятую
			# подсказка: для соединения преподавателей через запятую используйте string.join()
			dublicate_names_result.append(f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')


	return dublicate_names_result
import re
a = dublicate_names()[0]
print(a)
print(re.findall('Александр',a))

