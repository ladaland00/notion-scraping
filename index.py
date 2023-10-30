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
            if eventName ==None:
                continue 
            try:
                organizerType = tableData.find_element( By.XPATH,"./div/div/div[3]")
            except NoSuchElementException:
                opportunities = None           
            try:
                attendees = tableData.find_element( By.XPATH,"./div/div/div[4]")
            except NoSuchElementException:
                attendees = None                   
            try:
                opportunities = tableData.find_element( By.XPATH,"./div/div/div[5]")
            except NoSuchElementException:
                opportunities = None 
            try:
                attendance = tableData.find_element( By.XPATH,"./div/div/div[6]")
            except NoSuchElementException:
                attendance = None               
            try:
                startDate = tableData.find_element( By.XPATH,"./div/div/div[7]")
            except NoSuchElementException:
                startDate = None        
            try:
                endDate = tableData.find_element( By.XPATH,"./div/div/div[8]")
            except NoSuchElementException:
                endDate = None                       
            try:
                website = tableData.find_element( By.XPATH,"./div/div/div[9]")
            except NoSuchElementException:
                website = None   
            try:
                website = tableData.find_element( By.XPATH,"./div/div/div[10]")
            except NoSuchElementException:
                website = None  
            try:
                sponsorshipSite = tableData.find_element( By.XPATH,"./div/div/div[11]")
            except NoSuchElementException:
                sponsorshipSite = None 
            try:
                sponsorDownload = tableData.find_element( By.XPATH,"./div/div/div[12]")
            except NoSuchElementException:
                sponsorDownload = None 
            try:
                linkedIn = tableData.find_element( By.XPATH,"./div/div/div[12]")
            except NoSuchElementException:
                linkedIn = None 
            try:
                attendeeList = tableData.find_element( By.XPATH,"./div/div/div[13]")
            except NoSuchElementException:
                attendeeList = None 
            try:
                venue = tableData.find_element( By.XPATH,"./div/div/div[14]")
            except NoSuchElementException:
                venue = None 
            try:
                city = tableData.find_element( By.XPATH,"./div/div/div[15]")
            except NoSuchElementException:
                city = None 
            try:
                stateOrProvince = tableData.find_element( By.XPATH,"./div/div/div[16]")
            except NoSuchElementException:
                stateOrProvince = None 
            try:
                country = tableData.find_element( By.XPATH,"./div/div/div[17]")
            except NoSuchElementException:
                country = None 
            try:
                lowPriceNonMembers = tableData.find_element( By.XPATH,"./div/div/div[18]")
            except NoSuchElementException:
                lowPriceNonMembers = None 
            try:
                highPriceNonMembers = tableData.find_element( By.XPATH,"./div/div/div[19]")
            except NoSuchElementException:
                highPriceNonMembers = None 
            try:
                earlyBirdDeadline = tableData.find_element( By.XPATH,"./div/div/div[20]")
            except NoSuchElementException:
                earlyBirdDeadline = None 
            try:
                sponsorshipContactEmail = tableData.find_element( By.XPATH,"./div/div/div[21]")
            except NoSuchElementException:
                sponsorshipContactEmail = None 
            try:
                sponsorshipContactName = tableData.find_element( By.XPATH,"./div/div/div[22]")
            except NoSuchElementException:
                sponsorshipContactName = None 
            try:
                filesAndMedia = tableData.find_element( By.XPATH,"./div/div/div[23]")
            except NoSuchElementException:
                filesAndMedia = None 
            try:
                latestSponsorList = tableData.find_element( By.XPATH,"./div/div/div[24]")
            except NoSuchElementException:
                latestSponsorList = None 
            try:
                sponsorsAndExhibitors = tableData.find_element( By.XPATH,"./div/div/div[25]")
            except NoSuchElementException:
                sponsorsAndExhibitors = None 
            try:
                peekURL = tableData.find_element( By.XPATH,"./div/div/div[26]")
            except NoSuchElementException:
                peekURL = None 
            try:
                notes = tableData.find_element( By.XPATH,"./div/div/div[27]")
            except NoSuchElementException:
                notes = None 
            if eventName :
                cardData.append({
                    "eventName": eventName.text, 
                    "organizerType": organizerType.text.replace("\n", ", "),
                    "attendees": attendees.text.replace("\n", ", "),
                    "opportunities": opportunities.text.replace("\n", ", "),
                    "attendance":attendance.text,
                    "start": startDate.text,
                    "end": endDate.text,
                    "website":website.text,
                    "sponsorshipSite":sponsorshipSite.text,
                    "sponsorDownload":sponsorDownload.text,
                    "linkedIn":linkedIn.text,
                    "attendeeList":attendeeList.text,
                    "venue": venue.text,
                    "city":city.text,
                    "stateOrProvince":stateOrProvince.text,
                    "country":country.text,
                    "lowPriceNonMembers":lowPriceNonMembers.text,
                    "highPriceNonMembers":highPriceNonMembers.text,
                    "earlyBirdDeadline":earlyBirdDeadline.text,
                    "sponsorshipContactEmail":sponsorshipContactEmail.text,
                    "sponsorshipContactName":sponsorshipContactName.text,
                    "filesAndMedia":filesAndMedia.text,
                    "latestSponsorList":latestSponsorList.text,
                    "sponsorsAndExhibitors":sponsorsAndExhibitors.text,
                    "peekURL":peekURL.text,
                    "notes":notes.text
                    
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
