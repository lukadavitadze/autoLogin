from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(15)
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-603400432%3A1689453407950400&continue=https%3A%2F%2F"
           "m""ail.google.com%2Fmail%2F&ifkv=AeDOFXicju82LVYYll4-b3GDZhMXMjJE0RlpIMEcSNPOASqcN4SjVP47GiAfvNPXz8uPdT29An"
           "M""3oQ&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()
name = driver.find_element(by=By.ID, value="identifierId")
name.send_keys("#name.gamil.com#")
submit_button = driver.find_element(by=By.ID, value="identifierNext")
submit_button.click()
pw = driver.find_element(by=By.NAME, value="Passwd")
pw.send_keys("#PaSSWord#")
button_two = driver.find_element(by=By.ID, value="passwordNext")
button_two.click()
search = driver.find_element(by=By.ID, value=":np")
search.send_keys("lukinio2222@gmail.com")
button_two = driver.find_element(by=By.ID, value="button")
button_two.click()

