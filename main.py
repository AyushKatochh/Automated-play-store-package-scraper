from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def version(driver,link):
    driver.get(link)
    driver.implicitly_wait(5)
    name = driver.find_element(by=By.XPATH,value="/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span").text
    driver.implicitly_wait(5)
    driver.find_element(by=By.XPATH,
                        value="/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[2]/div/section/header/div/div[2]/button").click()
    driver.implicitly_wait(5)
    version = driver.find_element(by=By.XPATH,
                                  value="/html/body/div[5]/div[2]/div/div/div/div/div[2]/div[3]/div[1]/div[2]").text

    return name,version


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", service=Service(ChromeDriverManager().install()))
driver.get("https://play.google.com/store/apps")
driver.implicitly_wait(5)
top=driver.find_elements(by=By.CLASS_NAME, value="Si6A0c")
sol={}
links = [elem.get_attribute('href') for elem in top]
for link in links:
    key,value=version(driver,link)
    sol[key]=value
print(sol)
