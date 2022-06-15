from tkinter import PAGES
import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.co.uk/Sony-Full-Frame-Mirrorless-Real-time-Vari-angle/dp/B09JPCNS3X/ref=sr_1_2?crid=20NNB4OVL4ED5&keywords=sony+a7&qid=1655312001&sprefix=sony+a%2Caps%2C98&sr=8-2"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

