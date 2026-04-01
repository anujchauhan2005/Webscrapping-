import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/amazon_laptops.csv")

print("Total Products:", len(df))

# Convert to string first
df["Price"] = df["Price"].astype(str)
df["Price"] = df["Price"].str.replace(",", "")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["Rating"] = df["Rating"].astype(str)
df["Rating"] = df["Rating"].str.extract(r'(\d+\.\d+)')
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

print("Average Price:", df["Price"].mean())
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())


# 1.Top 10 Most Expensive Laptops 
top_expensive = df.sort_values("Price", ascending=False).head(10)
print("\nTop 10 Most Expensive Laptops:")
print(top_expensive[["Product_Name", "Price", "Rating"]])

# 2.Top Rated Laptops
'''top_rated = df.sort_values("Rating", ascending=False).head(10)
print("\nTop Rated Laptops:")
print(top_rated[["Product_Name", "Price", "Rating"]])'''


# 3.Brand Analysis (HP / Dell / Lenovo)

'''def get_brand(name):
    brands = ["HP", "Dell", "Lenovo", "ASUS", "Acer", "Apple"]
    for b in brands:
        if b.lower() in name.lower():
            return b
    return "Other"

df["Brand"] = df["Product_Name"].apply(get_brand)

print("\nBrand Counts:")
print(df["Brand"].value_counts())'''