from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

############################################################################

# если выдает ошибку, то вместо driver = webdriver.Chrome() пишем:

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(executable_path = ChromeDriverManager().install()) 

# так ну короче прога скачает и все крутямбово

#############################################################################

driver = webdriver.Chrome() # а как иначе-то, врубаем хром
driver.get('https://rankyourbrain.com/mental-math/mental-math-test-easy/countdown') # открываем сайт
sleep(6) # ждем каунтдаун (можно по-другому, но мне так нравится, код пишу я, а не ты :>)
try: # чтобы прога не вылетела
    while True: # ну ясно, пока можем - "решаем"
        x = int(eval(driver.find_element_by_xpath('//span[@id="beforeAnswer"]').text[:-2])) # находим элемент в котором наш вопрос, получаем его текст без "=", решаем
        # print(x) # ну если хотите побыть хацкерменами
        y = driver.find_element_by_xpath('//input[@id="answer"]').send_keys(x) # записываем в инпут (сайт сам жмет энтер)
except: # оу 
    print('все') # ну собственно если кончилось веселье
input() # чтобы не закрылась прога
