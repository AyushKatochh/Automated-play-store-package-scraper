from selenium import webdriver
import mail
import database
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def version(driver):
    driver.implicitly_wait(5)
    name = driver.find_element(by=By.XPATH,value="/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span").text

    driver.implicitly_wait(5)
    driver.find_element(by=By.XPATH,
                        value="/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[2]/div/section/header/div/div[2]/button").click()
    driver.implicitly_wait(5)
    version = driver.find_element(by=By.CSS_SELECTOR,
                                  value="#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div:nth-child(3) > div:nth-child(1) > div.reAt0")
    date = driver.find_element(by=By.CSS_SELECTOR,
                                  value="#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div.G1zzid > div:nth-child(2) > div.reAt0")

    return name,version,date




package_name=input("enter package name:")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", service=Service(ChromeDriverManager().install()))
driver.get(f"https://play.google.com/store/apps/details?id={package_name}&hl=en_IN&gl=US")
driver.implicitly_wait(5)
name,version,date=version(driver)
database.add_playstore(name,version.text,date.text,package_name)
x=database.find_all(package_name,version.text)
if x==0:
    database.add_all(package_name,version.text,date.text)
elif x==1:
    print("no version change")
else:
    print("version changed")
    mail.mail(name,package_name,version.text, date.text)
    database.update_all(package_name,version.text, date.text)
