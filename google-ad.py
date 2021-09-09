import pandas as pd
import time
from requests_html import HTMLSession
from selenium import webdriver
from random import randint
from time import sleep
from datetime import datetime


#needs proxy for "search by country"

session = HTMLSession(browser_args=["--no-sandbox", '--user-agent=Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'])




ad_list = [] 

df_keywords = pd.read_csv('keywords.csv', index_col =None, header=0 ) #pull in the keywords out of a CSV

for keyword in df_keywords.Keyword:
    #loop through the keywords
    print(keyword)
    r = session.get('https://google.com.au/search?q='+keyword) #First page ads
    # r = session.get('https://google.com.au/search?q='+keyword+'&start=60')#6th? page ads

    #get the bottom ads
    ads = r.html.find('.uEierd')

    for ad in ads:
        ad_link = ad.find('.Krnil', first=True).absolute_links #link to landing page
        ad_link = next(iter(ad_link)) #need this since the result from above is set
        ad_headline = ad.find('span', first=True).text #headline of the ad
        ad_copy = ad.find('.MUxGbd', first=True).text #ad copy
        ad_list.append([keyword, ad_link, ad_headline, ad_copy]) #append data row to list
        sleep(randint(8,25))


df_ads = pd.DataFrame(ad_list, columns = ['keyword', 'ad_link', 'ad_headline', 'ad_copy'])

#timestamp so we dont overwrite or mix up with old CSV
now = datetime.now()
ts = now.strftime("%d-%m-%Y-%H-%M-%S")
#write out to CSV for reference needs to have the proxy country as part of the name
df_ads.to_csv('top-ads-'+str(ts)+'.csv')

#Creating png screenshot as well as webp screenshot
#Selenium loop thru dataframe to save PNGs into "Screenshots" folder
#for index, row in df_ads.iterrows():
#    print('Index: ' + str(index) + ', Ad Link: ' + row['ad_link'])
#    options = webdriver.ChromeOptions()
#    options.add_argument('headless')
#    options.add_argument('window-size=1200x900')
#    options.add_argument("--allow-running-insecure-content")
#    options.add_argument('--ignore-certificate-errors')
#    browser = webdriver.Chrome(options=options)
#    browser.get(row['ad_link'])
#    browser.save_screenshot('screenshots/'+str(index)+'.png')
#    browser.quit()


#Extract html to save as archive then extract phone and email details


#Categorise site based on content


#Parsed WHOIS


#WP users if exist


#
