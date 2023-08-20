# See Version 2019 for handling time selection
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import time
import sys

demo_delay=2
court=3
booking_time = "15:00"

url = "https://i.cuhk.edu.cn/views/cbmapp/form/sitereservation/appointment?orderType=tch_psn&fieldTypeId=1100"
browser = wd.Firefox()
# browser = wd.Chrome()
browser.get(url)
browser.implicitly_wait(10)

#
# login
#
user=browser.find_element(By.ID, "username")
pwd=browser.find_element(By.ID, "password")
login=browser.find_element(By.ID, "btn-login")
user.clear()
pwd.clear()

time.sleep(demo_delay)
user.send_keys("kinleylam")
user.send_keys(Keys.TAB)

# wait for the booking page
wait = WebDriverWait(browser, 30)
element = wait.until(EC.title_contains('Booking'))

# Version 2021
con=browser.find_element(By.CLASS_NAME, "gridArea")
timecol = con.find_element(By.CLASS_NAME, "timeCol")
# The names of the booking courts
fieldnames = con.find_elements(By.CLASS_NAME, "fieldNameCol")
# The booking layout table (including the header and booking courts)
gridrows = con.find_elements(By.CLASS_NAME, "gridLine")

times=timecol.find_elements(By.CLASS_NAME, 'timeColItem')
slots=gridrows[court-1].find_elements(By.CLASS_NAME, 'gridColItem')

print(len(fieldnames),len(gridrows),len(times))

def get_slot_number(time):
    hr = int(time.split(':')[0])
    slot = (hr-7)*2
    return slot

num = get_slot_number(booking_time)
slot=slots[num]
print('slot',num)
time.sleep(demo_delay)
slot.click()
time.sleep(demo_delay*2)

# Telephone
form = browser.find_element(By.CLASS_NAME, "rightTarget")
tel = form.find_element(By.XPATH, '//input[@type="text"]')
time.sleep(demo_delay)
tel.send_keys('x73845')

# Description
time.sleep(demo_delay)
tel.send_keys(Keys.TAB)
current=browser.switch_to.active_element
current.send_keys('hello world')

# Skip to head count
time.sleep(demo_delay)
for x in range(4):
    current.send_keys(Keys.TAB)
    current=browser.switch_to.active_element
    time.sleep(demo_delay)

# head count
# current.send_keys(Keys.TAB)
# current=browser.switch_to.active_element
current.send_keys("2")

# Booking details
current.send_keys(Keys.TAB)
current=browser.switch_to.active_element
time.sleep(demo_delay)
current.send_keys("A booking demo for CSC1002 !!!!!") 

# booking confirmation
btn=form.find_element(By.CLASS_NAME, "ant-btn")
#btn.click()
print(btn)