import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

base_url = "http://xkcd.com/"

n = raw_input("Enter the comic number\n> ")

url = base_url + str(n)
page = requests.get(url).content
soup = BeautifulSoup(page, "lxml")
comicImageBlock = soup.find("div",{"id":"comic"})
comicImageTag = comicImageBlock.find("img")
comicURL = comicImageTag['src']
imageURL = 'https:' + comicURL
img_data = requests.get(imageURL)
i = Image.open(BytesIO(img_data.content))
save_file_name = 'xkcd' + str(n) + '.png'
i.save(save_file_name)

print "XKCD"+str(n)+" has been saved successfully"
