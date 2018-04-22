from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

#starting up web driver for chrome
option = webdriver.ChromeOptions()
option.add_argument('--incognito')

driver= webdriver.Chrome()
driver.get("https://247sports.com/Season/2003-Basketball/CompositeRecruitRankings?InstitutionGroup=HighSchool")

#elements we're parsing for
names = []
hometowns = []
positions = []
heights = []
weights = []

# #grabs all names
# divs = driver.find_elements_by_xpath('//div[contains(@class, "name")]//a')
# for div in divs:
# 	names.append(div.text)
# 	print div.text

# #grabs all hometowns
# homes = driver.find_elements_by_xpath('//div[contains(@class, "name")]//span')
# for home in homes:
# 	hometowns.append(home.text)
# 	print home.text

#grab heights
# pos = driver.find_elements_by_xpath('//ul[contains(@class, "metrics-list")]//li[contains(@class, "position")]')
# for po in pos:
# 	positions.append(pos.text)

# ht = driver.find_elements_by_xpath('//ul[contains(@class, "metrics-list")]//li[contains(@class, "height")]') 
# for h in ht:
# 	heights.append(h.text)

# wt = driver.find_elements_by_xpath('//ul[contains(@class, "metrics-list")]//li[contains(@class, "weight")]') 
# for w in wt:
# 	weights.append(w.text)