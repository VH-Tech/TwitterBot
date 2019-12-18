from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from getpass import getpass

import time

URL = "https://fedoramagazine.org/"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get(URL, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')
links = soup.find_all("a")

opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://twitter.com/login')

login = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
login.send_keys(input("Twitter ID/e-mail address: "))

paswd = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
paswd.send_keys(getpass("Twitter Password :"))

browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()

time.sleep(5)

tweet_box = browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')
str = str(links[8])

tweet_box.send_keys(str[str.index('href="')+6 : str.index('/"')])

ActionChains(browser) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.ENTER) \
    .perform()

print("Success!")