import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

pasta_atual = os.path.dirname(__file__)
pasta_do_chrome = f'{pasta_atual}\chromedriver.exe'

def make_chrome_browser(*args: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if args is not None:
        for option in args:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=pasta_do_chrome)
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    return browser

if __name__ == '__main__':
    # Exemplo
    options = ('--disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)

    browser.get('https://www.youtube.com/')
    sleep(2)
    browser.find_element(By.NAME, 'search_query').click()
    browser.find_element(By.NAME, 'search_query').send_keys('somewhere over the rainbow', Keys.ENTER)
    sleep(2)
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Somewhere over the Rainbow').click()