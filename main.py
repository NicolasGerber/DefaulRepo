import requests as rq
from bs4 import BeautifulSoup
import smtplib
import os

my_email = os.environ.get("PYTHON_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

URL = "https://appbrewery.github.io/instant_pot/"


response = rq.get(url=URL, headers={"User-Agent": "Mozilla/5.0"})
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

nome = soup.find(name="span", class_="a-size-large product-title-word-break")
name = nome.getText()

preco = soup.find(name="span",class_="a-offscreen")
price = preco.getText()
promo = float(price.split("$")[1])

subject = "The Product you selected is at a good price!"
body = f"The product {name} is now available for just ${promo:.2f}!"
message = f"Subject: {subject}\n\n{body}"

if promo < 100.00:
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()#ENCRIPTADOR
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="nicolasgergerber@gmail.com",
                                msg=message.encode("utf-8"))
            print("Email Sent!")
    except Exception as e:
        print(f"Error, fail to send email: {e}")