
import requests
import sys
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

base_url = "http://xkcd.com/"

n = raw_input("Enter the comic number\n> ")

if n.isdigit() == False:
	print "Input is not a number"
	sys.exit() 

url = base_url + str(n)
page = requests.get(url).content
soup = BeautifulSoup(page, "lxml")
if soup.title.string == "404 - Not Found":
	print "Comic not found"
else:
	comicImageBlock = soup.find("div",{"id":"comic"})
	comicImageTag = comicImageBlock.find("img")
	comicURL = comicImageTag['src']
	imageURL = 'https:' + comicURL
	img_data = requests.get(imageURL)
	i = Image.open(BytesIO(img_data.content))
	save_file_name = 'xkcd' + str(n) + '.png'
	i.save(save_file_name)

	print "XKCD"+str(n)+" has been saved successfully"

	ch = raw_input("\nDo you want to open the image? yes or no\n> ")
	if ch == "y" or ch == "yes":
		print "Opening image"
		i.show()
	elif ch == "n" or ch == "no":
		exit()
	else:
		print "Invalid input"
