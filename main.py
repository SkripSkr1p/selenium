from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.regtorg.ru/")
browser.find_element(By.LINK_TEXT, "Регистрация").click()

ActionChains(browser).move_to_element(
    browser.find_element(By.CSS_SELECTOR, 'input[src="/imgs/but_reg.gif"]')
).perform()


sleep(3)
