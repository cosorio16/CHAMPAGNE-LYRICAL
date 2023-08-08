from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


driver = webdriver.Chrome()


driver.get("https://twitter.com/i/flow/login")


time.sleep(10)

campo_usuario = driver.find_element(By.NAME, "text")
username = ''
campo_usuario.send_keys(username)
campo_usuario.send_keys(Keys.ENTER)

time.sleep(10)


campo_password = driver.find_element(By.NAME, "password")
password = ''
campo_password.send_keys(password)
campo_password.send_keys(Keys.ENTER)


time.sleep(2)



for i in range(1, 21):
    driver.get('https://twitter.com/compose/tweet')
    time.sleep(10)

    post = driver.find_element(
        By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    texto = 'BEST ALBUM EVER #UTOPIA, #TRAVISSCOTT #CHAMPAGNELYRICS #FOLLOWUS'
    post.send_keys(texto)

    campo_archivo = driver.find_element(By.XPATH, "//input[@type='file']")
    ruta_imagen = os.path.abspath(f'{i}.jpg')
    campo_archivo.send_keys(ruta_imagen)
    time.sleep(5)

    boton_tweet = driver.find_element(
        By.XPATH, "//div[@data-testid='tweetButton']")
    driver.execute_script("arguments[0].click();", boton_tweet)

    time.sleep(5)
