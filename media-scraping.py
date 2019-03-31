import os, sys
from urllib.request import urlretrieve
from urllib.parse import urlparse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

profile = sys.argv[1]
savePath = len(sys.argv) > 2 and sys.argv[2] or os.path.dirname(__file__)
urlProfile = 'https://twitter.com/{}/media'.format(profile)
print(urlProfile)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
driver.get(urlProfile)

tombstoneButtons = driver.find_elements_by_css_selector('.Tombstone button.Tombstone-action')

for tombstoneButton in tombstoneButtons :
    tombstoneButton.click()

photoContainerImages = driver.find_elements_by_css_selector('.tweet .content .AdaptiveMedia .AdaptiveMedia-photoContainer img')

urls = []

for image in photoContainerImages:
    urls.append(image.get_attribute('src'))

for urlMedia in urls:
        
    pathProfile = os.path.join(savePath, profile)
    dirExsits = os.path.isdir(pathProfile)
    
    if not dirExsits:
        os.mkdir(pathProfile)

    parsedUrl = urlparse(urlMedia)    
    filename = os.path.basename(parsedUrl.path)    
    pathFile = '{}/{}'.format(pathProfile, filename)
    exists = os.path.isfile(pathFile)

    if not exists:
        urlretrieve(urlMedia, pathFile)


driver.close()
driver.quit()