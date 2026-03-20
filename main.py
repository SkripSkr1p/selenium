from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import string

def generate_z_email(min_z=1, max_z=30, domain="gmail.com"):
    name = 'z' * random.randint(min_z, max_z)
    return f"{name}@{domain}"
generate_z_email()
browser = webdriver.Chrome()
browser.get("https://www.regtorg.ru/")
browser.find_element(By.LINK_TEXT, "Регистрация").click()

def succes_registration(browser):
    ActionChains(browser).move_to_element(browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]')).perform()
    browser.find_element(By.NAME, "_name").send_keys('asdsadsadsadsad')
    browser.find_element(By.NAME, "_fio").send_keys('sadfsadsadsad')
    browser.find_element(By.NAME, "_login").send_keys(generate_z_email())
    browser.find_element(By.NAME, "_password").send_keys('123123')
    browser.find_element(By.NAME, "_password2").send_keys('123123')
    browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]').click()
#succes_registration(browser)


def succes_avtorisation(browser):
    browser.find_element(By.NAME, "login").send_keys('generate_z_email()')
    browser.find_element(By.NAME, "passwd").send_keys('123123')
    browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_in.gif"]').click()
#succes_avtorisation(browser)

def failed_registration(browser):
    ActionChains(browser).move_to_element(browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]')).perform()
    browser.find_element(By.NAME, "_name").send_keys('aaaa11111')
    browser.find_element(By.NAME, "_fio").send_keys('aaaaaa111111')
    browser.find_element(By.NAME, "_login").send_keys('zzzzzzzzzzzzzzz@')
    browser.find_element(By.NAME, "_password").send_keys('12345')
    browser.find_element(By.NAME, "_password2").send_keys('12345')
    browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]').click()
#failed_registration(browser)

def failed_avtorisation(browser):
    browser.find_element(By.NAME, "login").send_keys('zzzzz@')
    browser.find_element(By.NAME, "passwd").send_keys('123123')
    browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_in.gif"]').click()
#failed_avtorisation(browser)

def succes_registration_and_purchase_vertolet(browser):
    ActionChains(browser).move_to_element(browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]')).perform()
    browser.find_element(By.NAME, "_name").send_keys('aaaa11111111')
    browser.find_element(By.NAME, "_fio").send_keys('aaaaaa11111111')
    browser.find_element(By.NAME, "_login").send_keys(generate_z_email())
    browser.find_element(By.NAME, "_password").send_keys('121345')
    browser.find_element(By.NAME, "_password2").send_keys('121345')
    browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]').click()
    browser.find_element(By.LINK_TEXT, "Товары и услуги").click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".reply-button"))).click()

    browser.find_element(By.LINK_TEXT, "Бытовая техника").click()
    browser.find_element(By.LINK_TEXT, "Аудиотехника").click()
    browser.find_element(By.LINK_TEXT, "Front Row Guno - цифровая инфракрасная акустическая система").click()

succes_registration_and_purchase_vertolet(browser)

sleep(5)
browser.quit()
