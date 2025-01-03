from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.set_capability("unhandledPromptBehavior", "dismiss")

# PATH = "C:/Users/Heather/MU/Codes/web/auto_reserve_vbfield/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(options=options)
driver.get("https://rent.pe.ntu.edu.tw/member/?U=login")

# account information
accounts = [\
            ]
# todo: get accounts from .env


for account in accounts: 
  try:
    # enter account information
    user = driver.find_element(By.NAME, "Username")
    user.send_keys(account[0])
    user.click()
    time.sleep(2)
    pswd = driver.find_element(By.NAME, "Password")
    pswd.send_keys(account[1])
    time.sleep(2)
    
    # get all the way into the form
    driver.find_element(By.NAME, "LoginBtn").click()
    WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.LINK_TEXT, "會員專區"))
    )
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[@href="/venues/?K=89"]').click()
    WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.LINK_TEXT, "場地資訊"))
    )
    driver.find_element(By.CLASS_NAME, "F").click()
    WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.CLASS_NAME, "LightboxContent"))
    )
    driver.find_element(By.NAME, "Close").click()
    


    # select fields
    # driver.execute_script("window.scrollBy(0, 900);")
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//div[@d="2024-09-02"]/a[@title="18 ~ 20"]').click()

    # Logout
    WebDriverWait(driver, 300).until(
      EC.presence_of_element_located((By.NAME, "GoMember"))
    )
    driver.find_element(By.LINK_TEXT, "登出").click()
    WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.LINK_TEXT, "會員登入"))
    )
    driver.find_element(By.LINK_TEXT, "會員登入").click()
    WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.NAME, "LoginBtn"))
    )
  except:
    print("帳號 "+account[0]+" 未抽場成功")
    driver.get("https://rent.pe.ntu.edu.tw/member/?U=login")




# send_keys(Keys.RETURN)

print("抽場完成。正在離開自動抽場系統。")
driver.quit()
print("已離開自動抽場系統。祝好運\\|/")