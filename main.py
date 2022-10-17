import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from threading import Thread


def program(num):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=800,600")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    service = Service(executable_path="./chromedriver")

    driver = webdriver.Chrome(options=options, service=service)

    driver.get("https://calls.mail.ru/room/d421461f-d9d7-480c-ac19-62533a3f03b5")
    time.sleep(5)
    driver.find_element(By.XPATH, "//html/body/div[3]/div[2]/div/div/div[2]/div/div[4]/div/div/div/input").send_keys(
        f'Гость {num}')
    driver.save_screenshot(f'Перед_{num}.png')
    time.sleep(20)
    driver.find_element(By.XPATH, "//html/body/div[3]/div[2]/div/div/div[2]/div/button[2]/span").click()
    time.sleep(10000)


if __name__ == '__main__':
    N = int(input('Введите количество единовременных пользователей: '))
    thread_list = list()

    for i in range(N):
        t = Thread(name='Test {}'.format(i), target=program, args=(i,))
        t.start()
        time.sleep(15)
        print(t.name + ' started!')
        thread_list.append(t)

    for thread in thread_list:
        thread.join()
