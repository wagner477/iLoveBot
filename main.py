from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


link: str = "https://web.whatsapp.com"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 30)

message: str = "Eu te amo"


# Função para selecionar um elemento e clicar nele a partir do XPATH
def selectAndClick(path: str):
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, path)
    ))
    element.click()


driver.get(link)

selectAndClick('//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div')

while True:
    input = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         '''//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div
         [1]''')
    ))

    input.send_keys(message)

    selectAndClick(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
