# Dependencies
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time

# Function for scraping

def init_browser():
    # Create path and browser with chromedriver
    executable_path={'executable_path': '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    ### NASA Mars News
    # URL of page to be scraped
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(5)
    
    # Scrape page into Soup
    html=browser.html
    soup = bs(html, "html.parser")
    
    # Extract the latest news title and paragraph:
    article=soup.find("div", class_='list_text')
    title=article.find("div", class_="content_title")
    news_title=title.find("a").text
    news_p=article.find("div", class_ ="article_teaser_body").text
    
    #--------------------------------------------------------------------------------------------------------# 
    ### JPL Mars Space Images - Featured Image
    # URL of page to be scraped
    url_image='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(5)
    html_image=browser.html
    
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_image=bs(html_image, 'html.parser')

    # Extract the latest image:
    containers=soup_image.find_all("div",class_="img")
    for container in containers:
        img=container.find('img')["src"]
        img2=img.split('/')[4]
        img3=img2.split('-')[0]
    featured_image_url='https://www.jpl.nasa.gov/spaceimages/images/largesize/'+img3+'_hires.jpg'
    #--------------------------------------------------------------------------------------------------------# 
    ### Mars Weather
    # URL of page to be scraped
    url_tweet='https://twitter.com/marswxreport'
    browser.visit(url_tweet)
    time.sleep(5)
    html_tweet=browser.html
    
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_tweet=bs(html_tweet, 'html.parser')
    # Loop through latest tweets and find the tweet that has weather information
    tweet_container=soup_tweet.find_all('span')
    for tweet in tweet_container: 
        weather=tweet.text
        if 'InSight sol' in weather:
            mars_weather=weather
            break
        else: 
            pass

    #--------------------------------------------------------------------------------------------------------# 

    ### Mars Facts
    # URL of page to be scraped
    url_facts='https://space-facts.com/mars/'

    # Extract the facts to dataframe:
    tables=pd.read_html(url_facts)
    profile=pd.DataFrame(tables[0])
    profile=profile.rename(columns={0:"Facts", 1:"Results"}).set_index('Facts')

    # Convert to html
    html_table=profile.to_html()

    #--------------------------------------------------------------------------------------------------------# 
    
    ### Mars Hemispheres
    # URL of page to be scraped
    url_hem='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hem)
    time.sleep(5)
    html_hem=browser.html
    
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_hem=bs(html_hem, 'html.parser')

    # Extract image urls and their titles
    hemisphere_image_urls=[]
    dict={}
    results=soup_hem.find_all('div', class_='item')
    for result in results:
        desc=result.find('div', class_='description')
        a=desc.find('a')
        l=a['href'].split('/')[5]
        link='http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/' + l + '.tif/full.jpg'
        title_hem=a.find('h3').text
        dict={'Title': title_hem, 'img_url': link}
        hemisphere_image_urls.append(dict)
    
    #--------------------------------------------------------------------------------------------------------# 
    #--------------------------------------------------------------------------------------------------------# 

    # Store data in a dictionary
    data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url":featured_image_url,
        "mars_weather":mars_weather,
        "html_table": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()
    
    # Return results
    return data