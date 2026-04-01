from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

print("Opening Amazon...")

driver = webdriver.Chrome()

names=[]
prices=[]
ratings=[]

pages = 7   # 7 pages ≈ 200 products

for page in range(1, pages+1):

    url=f"https://www.amazon.in/s?k=laptops&page={page}"
    print("Scraping page:",page)

    driver.get(url)
    time.sleep(5)

    products = driver.find_elements(By.CSS_SELECTOR,"div.s-result-item")

    for product in products:

        try:
            name = product.find_element(By.CSS_SELECTOR,"h2 span").text
        except:
            continue

        try:
            price = product.find_element(By.CSS_SELECTOR,"span.a-price-whole").text
        except:
            price="N/A"

        try:
            rating = product.find_element(By.CSS_SELECTOR,"span.a-icon-alt").text
        except:
            rating="N/A"

        names.append(name)
        prices.append(price)
        ratings.append(rating)

driver.quit()

df=pd.DataFrame({
    "Product_Name":names,
    "Price":prices,
    "Rating":ratings
})

print("Total products scraped:",len(df))

df.to_csv("data/amazon_laptops.csv",index=False)

print("Data saved successfully")
