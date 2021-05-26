#!/usr/bin/env python3

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

urls = "https://www.fun-diffusion.com/82-flotteurs-occasion?id_category=82&n=24" # Replace that url if you want

response = requests.get(urls)

soup = BeautifulSoup(response.content, "html.parser")

titles = []
prices = []

anonces_div = soup.find_all(class_='product-container')

for container in anonces_div:                                                    # Check the guide to understand how to scrap the information you need from a site

    name = container.h5.a.text
    titles.append(name)

    price = container.find(class_='price product-price').text
    prices.append(price)

board = pd.DataFrame({
    'titles': titles,
    'prices': prices
})

board.to_csv('board.csv')