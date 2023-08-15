# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.
import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self,foldername):
        folder_url = str('https://cloud-api.yandex.net/v1/disk/resources?path=%2F'+foldername)
        headers = self.get_headers()
        response = requests.put(folder_url, headers=headers)
        response.raise_for_status()
        return response.status_code





if __name__ == '__main__':


    # запрос входных данных
    token = input('Введите токен с Полигона Яндекс.Диска ')
    foldername = input('Введите название папки ')

    # создание папки на Яндекс.Диск
    folder = YandexDisk(token).create_folder(foldername)


