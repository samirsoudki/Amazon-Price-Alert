web_url = "https://www.amazon.com/Pioneer-DJ-Controller-DDJ-800/dp/B07QMQ5YGK/ref=pd_sbs_1/143-9296653-0622846?pd_rd_w=iNhJF&pf_rd_p=755df9fc-1b62-4c8c-831e-91a7f8454d75&pf_rd_r=3Q6NQ39TZC857JRSXGWN&pd_rd_r=e4821db6-7117-4836-962e-c4ab86fc89e6&pd_rd_wg=a73HG&pd_rd_i=B07QMQ5YGK&psc=1"
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
Sender = "samirsoudkitesting@gmail.com"
Receiver = "samirsoudkitesting@gmail.com"
password = "Summer2014?"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
accept_lang = "ru-UA,ru-RU;q=0.9,ru;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5,uk;q=0.4"
headers = {
    "User-Agent": user_agent,
    "Accept-Language": accept_lang
}
response = requests.get(web_url, headers=headers)
response.raise_for_status()
web_code = response.text

soup = BeautifulSoup(web_code, "lxml")
pp = soup.find(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
p = pp.text
p_2 = p.split("$")
p_3 = float(p_2[1])
price = format(p_3, '.2f')
Price = float(price)
print(type(Price))
budget_price = 900
message = f"""From: From Person <samirsoudkitesting@gmail.com>
To: To Person <samirsoudkitesting@gmail.com>
Subject: Amazon Price Alert

DDJ-800 Price Drop!
The Price of the DDJ-800 is ${Price}0.
Here is the link to buy it: {web_url}
"""
if Price <= budget_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=Sender, password=password)
        connection.sendmail(
            from_addr=Sender,
            to_addrs=Receiver,
            msg=message,
        )
    print("it worked")

else:
    print("did not work")



