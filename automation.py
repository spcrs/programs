from cgitb import html
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.flipkart.com/wishlist?link=home_wishlist")
#print(soup.prettify())
#//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input
# _2IX_2- VJZDxU
#content = driver.page_source

driver.find_element_by_class_name('_2IX_2-').send_keys('7904905394')
driver.find_element_by_css_selector('input[type=password]').send_keys('sankar2001')
driver.find_element_by_class_name("_2KpZ6l").submit()
content=driver.page_source
soup = BeautifulSoup(content,features="html.parser")
print(soup.find("col-10-12"))
#col col-10-12