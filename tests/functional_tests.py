from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000")
time.sleep(5)
print(browser.title)

# from selenium import webdriver
#
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
#
# service = ChromeService(executable_path=ChromeDriverManager().install())
#
# driver = webdriver.Chrome(service=service)