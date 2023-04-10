from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json
opt = Options()
opt.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=opt)
driver.get("https://aviso.bz/login")
print("please wait...")
time.sleep(3)


#load cookies
with open('cookie.json', 'r') as f:
    cookies = json.load(f)
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
time.sleep(1)









def youtube():
    window_before = driver.window_handles[0]
    driver.get("https://aviso.bz/work-youtube")
    time.sleep(3)
    coin = driver.find_element(By.ID,"new-money-ballans").text
    print(coin)
    text = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[3]/div/span[1]").text
    wait = text[0:2]
    print(wait)
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/span[1]").click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    time.sleep(12)
    acttion = ActionChains(driver)
    acttion.send_keys(Keys.TAB)
    time.sleep(0.5)
    acttion.send_keys(Keys.TAB)
    time.sleep(0.5)
    acttion.send_keys(Keys.TAB)
    time.sleep(0.5)
    acttion.send_keys(Keys.TAB)
    time.sleep(0.5)
    acttion.send_keys(Keys.TAB)
    time.sleep(0.5)
    acttion.send_keys(Keys.ENTER)
    time.sleep(0.5)
    acttion.perform()
    new_wait = int(wait) + 10
    time.sleep(new_wait)
    driver.close()
    driver.switch_to.window(window_before)
    print("dione..")
    time.sleep(2)


    
driver.get("https://aviso.bz/work-youtube")
check = driver.current_url
time.sleep(2)
print(check)
if check == "https://aviso.bz/work-youtube":
    while True:
        try:
            youtube()
            time.sleep(1)
        except:
            continue
else:
    print("no")
   
