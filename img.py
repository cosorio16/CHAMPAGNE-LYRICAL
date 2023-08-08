from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()


driver.get("https://twitter.com/i/flow/login")

time.sleep(10)

campo_busqueda = driver.find_element(By.NAME, "text")
username = ''
campo_busqueda.send_keys(username)
campo_busqueda.send_keys(Keys.ENTER)

time.sleep(10)

campo_busqueda = driver.find_element(By.NAME, "password")
password = ''
campo_busqueda.send_keys(password)
campo_busqueda.send_keys(Keys.ENTER)
time.sleep(5)


for i in range(1, 21):

    driver.get('https://twitter.com/compose/tweet')
    time.sleep(15)

    campo_texto = driver.find_element(
        By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    texto = 'BEST ALBUM EVER #UTOPIA, #TRAVIS SCOTT #CHAMPAGNELYRICS #FOLLOWUS'
    campo_texto.send_keys(texto)

    time.sleep(2)

    campo_archivo = driver.find_element(By.XPATH, "//input[@type='file']")
    ruta_imagen = os.path.abspath(f'{i}.jpg')

    campo_archivo.send_keys(ruta_imagen)
    time.sleep(5)

    boton_tweet = driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div')
    time.sleep(5)
    boton_tweet.click()

    time.sleep(10)
