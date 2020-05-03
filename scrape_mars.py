{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Web Scraping - Mission to Mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import requests\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 394,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create path and browser with chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Perseverance Rover Will Look at Mars Through These 'Eyes'\n",
      "A pair of zoomable cameras will help scientists and rover drivers with high-resolution color images.\n"
     ]
    }
   ],
   "source": [
    "# URL of page to be scraped\n",
    "url=\"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup=bs(html, 'html.parser')\n",
    "\n",
    "# Extract the latest news title and paragraph:\n",
    "article=soup.find(\"div\", class_='list_text')\n",
    "title=article.find(\"div\", class_=\"content_title\")\n",
    "news_title=title.find(\"a\").text\n",
    "news_p=article.find(\"div\", class_ =\"article_teaser_body\").text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url_image='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url_image)\n",
    "time.sleep(1)\n",
    "html_image=browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup_image=bs(html_image, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 293,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23818_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "# Extract the latest image:\n",
    "containers=soup_image.find_all(\"div\",class_=\"img\")\n",
    "img=container.find('img')[\"src\"]\n",
    "img2=img.split('/')[4]\n",
    "img3=img2.split('-')[0]\n",
    "featured_image_url='https://www.jpl.nasa.gov/spaceimages/images/largesize/' + img3 +'_hires.jpg'\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 366,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url_tweet='https://twitter.com/marswxreport'\n",
    "browser.visit(url_tweet)\n",
    "time.sleep(1)\n",
    "html_tweet=browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup_tweet=bs(html_tweet, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 370,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 508 (2020-05-01) low -92.2ºC (-134.0ºF) high -2.4ºC (27.7ºF)\n",
      "winds from the SW at 5.1 m/s (11.3 mph) gusting to 15.8 m/s (35.3 mph)\n",
      "pressure at 6.80 hPa\n"
     ]
    }
   ],
   "source": [
    "# Loop through latest tweets and find the tweet that has weather information\n",
    "for tweet in tweet_container: \n",
    "    mars_weather=tweet.text\n",
    "    if 'InSight' in mars_weather:\n",
    "        print(mars_weather)\n",
    "        break\n",
    "    else: \n",
    "        pass\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 392,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url_facts='https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 393,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Results</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Facts</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Results\n",
       "Facts                                              \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 393,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extract the facts to dataframe:\n",
    "tables=pd.read_html(url_facts)\n",
    "profile=pd.DataFrame(tables[0])\n",
    "profile=profile.rename(columns={0:\"Facts\", 1:\"Results\"}).set_index('Facts')\n",
    "profile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 391,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Results</th>\\n    </tr>\\n    <tr>\\n      <th>Facts</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Equatorial Diameter:</th>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>Polar Diameter:</th>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Distance:</th>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Period:</th>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>Surface Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>First Record:</th>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>Recorded By:</th>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 391,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert to html\n",
    "html_table=profile.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 395,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url_hem='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url_hem)\n",
    "time.sleep(1)\n",
    "html_hem=browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup_hem=bs(html_hem, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 421,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extract image urls and their titles\n",
    "hemisphere_image_urls=[]\n",
    "dic={}\n",
    "results=soup_hem.find_all('div', class_='item')\n",
    "for result in results:\n",
    "    desc=result.find('div', class_='description')\n",
    "    a=desc.find('a')\n",
    "    l=a['href'].split('/')[5]\n",
    "    link='http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/' + l + '.tif/full.jpg'\n",
    "    title=a.find('h3').text\n",
    "    dict={'Title': title, 'img_url': link}\n",
    "    hemisphere_image_urls.append(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 424,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'Title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'Title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'Title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'Title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 424,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the list\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
