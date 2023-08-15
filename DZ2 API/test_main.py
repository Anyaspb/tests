from unittest import TestCase
from main import YandexDisk

# задать для теста
token = ''
foldername = ''


class TestYandexDisk(TestCase):
    def test_create_folder(self):
        res = YandexDisk(token).create_folder(foldername)
        self.assertEqual(res, 201, msg ='папка создана')











