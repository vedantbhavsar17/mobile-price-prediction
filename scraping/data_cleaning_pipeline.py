#Code is cleaned after exported from Jupyter notebook 

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# --------------------------------
# Load HTML & Scrape Data
# --------------------------------
with open("smartprix.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "lxml")

products = soup.find_all("div", class_="sm-product has-tag has-features has-actions")

name, price, rating, sim, processor, ram, battery, display, camera, card, os = ([] for _ in range(11))

for p in products:
    try: name.append(p.find("h2").text)
    except: name.append(np.nan)

    try: price.append(p.find("span", class_="price").text)
    except: price.append(np.nan)

    try: rating.append(p.find("div", class_="score").find("b").text)
    except: rating.append(np.nan)

    specs = p.find("ul", class_="sm-feat specs")
    specs = specs.find_all("li") if specs else []

    def get(i):
        try: return specs[i].text
        except: return np.nan

    sim.append(get(0))
    processor.append(get(1))
    ram.append(get(2))
    battery.append(get(3))
    display.append(get(4))
    camera.append(get(5))
    card.append(get(6))
    os.append(get(7))

df = pd.DataFrame({
    "name": name,
    "price": price,
    "rating": rating,
    "sim": sim,
    "processor": processor,
    "ram_GB": ram,
    "battery": battery,
    "display": display,
    "camera": camera,
    "card": card,
    "os": os
})

# --------------------------------
# Basic Cleaning
# --------------------------------
df["price"] = df["price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["name"] = df["name"].str.split("(").str[0].str.strip().str.title()
df.insert(0, "brand", df["name"].str.split().str.get(0).str.title())

df = df[~df.duplicated()]

# --------------------------------
# Remove Feature Phones (Your Logic)
# --------------------------------
low_price_index = df.sort_values(by="price").head(46).index
df.drop(low_price_index, inplace=True)

# --------------------------------
# SIM Feature Flags
# --------------------------------
df["is_5g"] = df["sim"].str.contains("5G", na=False)
df["is_nfc"] = df["sim"].str.contains("NFC", na=False)
df["is_ir_blaster"] = df["sim"].str.contains("IR Blaster", na=False)

# --------------------------------
# Processor Features
# --------------------------------
df["processor_brand"] = df["processor"].str.split().str.get(0)
df["processor_variant"] = df["processor"].str.split(",").str.get(0)
df["core"] = df["processor"].str.split(",").str.get(1)
df["processor_speed"] = df["processor"].str.split(",").str.get(2).str.split().str.get(0)

# --------------------------------
# RAM & Storage
# --------------------------------
df["ram"] = df["ram_GB"].str.split().str.get(0)
df["internal_memory"] = df["ram_GB"].str.split(",").str.get(1).str.split().str.get(0)

df["internal_memory"].replace("1", "1024", inplace=True)

# --------------------------------
# Battery Features
# --------------------------------
df["battery_size"] = df["battery"].str.split().str.get(0)
df["fast_charge"] = df["battery"].str.contains("Fast", na=False)
df["charging_speed"] = df["battery"].str.split("with").str.get(1).str.split("W").str.get(0)
df["charging_speed"].replace("Fast Charging", "20", inplace=True)
df["charging_speed"].fillna("20", inplace=True)

# --------------------------------
# Display Features
# --------------------------------
df["display_size"] = df["display"].str.split().str.get(0)
df["refresh_rate"] = (
    df["display"]
    .str.split(",").str.get(2)
    .str.split().str.get(0)
    .fillna("60")
)

# --------------------------------
# Camera Features
# --------------------------------
df["rear_mp"] = df["camera"].str.split("&").str.get(0).str.split().str.get(0)
df["front_mp"] = df["camera"].str.split("&").str.get(1).str.split().str.get(0)

# --------------------------------
# Final Cleanup
# --------------------------------
df["os"].fillna("Android", inplace=True)
df["card"].fillna("Memory Card Not Supported", inplace=True)

df = df.dropna(subset=["price", "ram", "battery_size"])
df.reset_index(drop=True, inplace=True)

# --------------------------------
# Save Final Dataset
# --------------------------------
df.to_csv("mobiledata.csv", index=False)

print("Final dataset saved as mobiledata.csv")
print("Final shape:", df.shape)