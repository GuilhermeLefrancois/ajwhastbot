from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Bot:
    contatos = []
    mensagem = ""
    driver = None

    def __init__(contatos, mensagem):
        try:
            Bot.contatos = contatos.split(',')
            Bot.mensagem = mensagem
            print(Bot.contatos)
            print(Bot.mensagem)
            Bot.driver = webdriver.Chrome(ChromeDriverManager().install())
            Bot.driver.get('https://web.whatsapp.com/')        
        except Exception as exp:
            print(exp.args)

    def send():
        try:
            time.sleep(5)
            print("Entrei")
            print("--------------------------------")
            for contato in Bot.contatos:
                print(contato)
                Bot.buscarContato(contato)
                Bot.enviarMensagem(Bot.mensagem)
        except Exception as exp:
            Bot.send()

    def buscarContato(contato):
        campo = Bot.driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
        time.sleep(3)
        campo.click()
        campo.send_keys(contato)
        campo.send_keys(Keys.ENTER)

    def enviarMensagem(mensagem):
        campo = Bot.driver.find_elements(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')[1]
        time.sleep(3)
        campo.click()
        campo.send_keys(mensagem)
        campo.send_keys(Keys.ENTER)

        