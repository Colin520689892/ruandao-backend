from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def search_furniture_stores(keyword="家具"):

    

    search_url = f"https://www.google.com/search?q={keyword}+店铺"


    driver = webdriver.Chrome()
    driver.get(search_url)


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
    )


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
    )


    html_content = driver.page_source


    soup = BeautifulSoup(html_content, 'html.parser')
    store_links = []

 
    for link in soup.find_all('a', href=True):
        if "https://www.google.com/maps/place/" in link['href']:
            store_links.append(link['href'])

   
    # driver.quit()

    return store_links

store_links = search_furniture_stores()


for link in store_links:
    print(link)