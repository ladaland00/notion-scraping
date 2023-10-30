import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

import urllib.parse as urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# proxy
# define custom options for the Selenium driver
options = Options()
# free proxy server URL
# proxy_server_url = "157.245.97.60"
# options.add_argument(f'--proxy-server={proxy_server_url}')

# Define search parameters
homeUrl = 'https://eventhunter.notion.site/eventhunter/9c233ae8a2544cb79631cc714ebe002d?v=5be9e321daa744a6801f3cab9008f0fd'

# Initialize an instance of the chrome driver (browser)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Visit your target site
print("Go to Notion")
print("Loading...")
driver.get(homeUrl)

# Type action
actions = ActionChains(driver)

cardData=[]
# Scroll down the page for the specified number of times
try:
    scroller = wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,".notion-scroller.vertical")))
    print("found")        
    scroll_pixels = 4000  
    while True:
        
        driver.execute_script("arguments[0].scrollTop += arguments[1];", scroller, scroll_pixels)
        time.sleep(2)
        scrollTop = driver.execute_script(
            "return arguments[0].scrollTop", scroller
        )
        offsetHeight = driver.execute_script(
            "return arguments[0].offsetHeight", scroller
        )
        scrollHeight = driver.execute_script(
            "return arguments[0].scrollHeight", scroller
        )
        print("is_scrollable",scrollHeight,scrollTop,offsetHeight)

        if  scrollTop+offsetHeight>=scrollHeight:
            print("Reached the end of the scrollable div.")
            break
        
except TimeoutException:
    print("Not found")
try:  
    tableAllData = driver.find_elements(
    By.XPATH, "//*[@id='notion-app']/div/div[1]/div/div[1]/main/div/div[5]/div/div/div[1]/div[3]/div")
    for index, tableData in enumerate(tableAllData):
        try:  
            eventName = tableData.find_element( By.XPATH,"./div/div/div[2]/div/div/a/span")
            print(eventName.text)
            organizerType = tableData.find_element( By.XPATH,"./div/div/div[3]")
            print(organizerType.text)
            attendees = tableData.find_element( By.XPATH,"./div/div/div[4]")
            print(attendees.text)
            opportunities = tableData.find_element( By.XPATH,"./div/div/div[5]")
            print(opportunities.text)
            if eventName :
                cardData.append({
                    "eventName": eventName.text, 
                    "organizerType": organizerType.text.replace("\n", ", "),
                    "attendees": attendees.text.replace("\n", ", "),
                    "opportunities": opportunities.text.replace("\n", ", ")
                })
            
        except NoSuchElementException:
            print("Not found eventName")
except NoSuchElementException:
    print("Not found table all data")
# Save the scraped data to a file
outputFileName = "scrapedData.json"
print("cardData", cardData)
with open(outputFileName, "w") as file:
    json.dump({"data": cardData}, file)

print("Data saved to", outputFileName)

# Release the resources allocated by Selenium and shut down the browser
print("Close browser")
driver.quit()
