import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from threading import Thread


def program(num, link):
    # Подключение опций
    options = Options()
    options.headless = True
    options.add_argument('--window-size=800,600')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    # Разрешение использования микрофона и камеры
    options.set_preference("permissions.default.microphone", 1)
    options.set_preference("permissions.default.camera", 1)

    # Путь к драйверу
    service = Service(executable_path=r"C:\BotPars\geckodriver.exe")
    driver = webdriver.Firefox(options=options, service=service)

    # Ссылка на необходимый ресурс
    driver.get(link)
    time.sleep(10)
    driver.find_element(By.XPATH, "//html/body/div[3]/div[2]/div/div/div[2]/div/div[4]/div/div/div/input").send_keys(
        f'Гость {num}')  # Заполнение имени
    # Вход без использования микрофона и камеры
    driver.find_element(By.XPATH, "//html/body/div[3]/div[2]/div/div/div[2]/div/label/div").click()
    driver.find_element(By.XPATH, "//html/body/div[3]/div[2]/div/div/div[2]/div/button[2]/span").click()
    time.sleep(5)


if __name__ == '__main__':
    print('####Программа проверки одновременной работы "Видео звонок" от маил.ру####\n')
    # Ввод n одновременно работающих процессов
    n = int(input('Введите количество единовременных пользователей: '))

    # Ввод подходящей ссылки
    url = ''
    while url.find('https://calls.mail.ru/room/') < 0:
        url = input('Введите ссылку на звонок("https://calls.mail.ru/room/d421461f-d9d7-480c-ac19-62533a3f03b5"): ')

    thread_list = list()

    # Цикл создания n потоков
    for i in range(n):
        t = Thread(name='Test {}'.format(i), target=program, args=(i, url,))  # Создание объекта потока
        t.start()  # Запуск потока
        time.sleep(10)
        print(t.name + ' started!')  # Сообщение о потоке
        thread_list.append(t)  # Добавление потока в список

    # Цикл ожидания завершения выполнения всех потоков
    for thread in thread_list:
        thread.join()
