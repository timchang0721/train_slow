#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time
from datetime import datetime, timedelta
import pydirectinput
#from PIL import Image 
# import pytesseract
# def checkprice():
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     im = pyautogui.screenshot(region=(298,667, 200,45))
#     im.save('123.png')
#     img = Image.open("123.png")
#     text = pytesseract.image_to_string(img, lang='eng')
#     #text.split('\n')
#     #ans = text.split('\n')[0].replace(",","")
#     #ans = ans.split('\n')[0].replace(".","")
#     #ans = re.sub(r'\D', '', ans)
#     print(text)
#     return text
driver = webdriver.Chrome()
# 設定隱式等待時間為10秒
driver.implicitly_wait(1000)

URL = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query"
 
identitycard = "A129843599"
departure = "1000-臺北"
arrive = "7000-花蓮"
num_ticket = "4"
godate ="20240627"
num_train_go = "408"
returndate = "20240627"
num_train_return = "447"

def wait_until_noon():  #等待到午夜12點
    now = datetime.now()
    target_time = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if now.minute >= 0:
        target_time += timedelta(days=1)
    wait_time = (target_time - now).total_seconds()
    time.sleep(wait_time)

#開啟網頁
driver.get(URL)

#視窗最大化
#driver.maximize_window()


button2 = driver.find_element(By.NAME,"pid")
button2.send_keys(identitycard)
button3 = driver.find_element(By.NAME,"startStation")
button3.send_keys(departure)
button4 = driver.find_element(By.NAME,"endStation")
button4.send_keys(arrive)
button1 = driver.find_element(By.XPATH,"html/body/div[4]/div[5]/div/form/div[1]/div[1]/div[5]/div/label[2]")
button1.click()
button5 = driver.find_element(By.ID,"normalQty")
button5.clear()
button5.send_keys(num_ticket)
time.sleep(0.3)
button6 = driver.find_element(By.ID,"rideDate1")
button6.clear()
button6.send_keys(godate)
button7 = driver.find_element(By.ID,"trainNoList1")
button7.send_keys(num_train_go)
button8 = driver.find_element(By.ID,"rideDate2")
button8.send_keys(returndate)
button9 = driver.find_element(By.ID,"trainNoList4")
button9.send_keys(num_train_return)
#wait_until_noon()
iframe = driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/form/div[4]/div/div[1]/div/div/div/iframe')
driver.switch_to.frame(iframe)
target_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]')
target_element.click()
time.sleep(0.3)
driver.switch_to.default_content()
button10 = driver.find_element(By.XPATH,"/html/body/div[4]/div[5]/div/form/div[4]/input[2]")
button10.click()
time.sleep(100)

