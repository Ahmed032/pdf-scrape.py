from bs4 import BeautifulSoup
import re
import requests

def main():
	#Setting the website to be scraped
	req = "https://search.usa.gov/search?v%3Aproject=firstgov&query=pdf&affiliate=nws.noaa.gov"
	#Setting the headers to be able to retrive data
	#Will get an error if removed
	headers = {'User-Agent':'Chrome/39.0.2171.71'}
	#Requests the req variable from above
	page = requests.get(req)
	#Turning it into a BeautifulSoup object
	soup = BeautifulSoup(page.text, "lxml")
	#Opening the file I will write to
	file = open("./pdfsearch.txt", "wt")
	#A counter for the number of pulled links
	i = 0
	#Finding ALL of the a tags
	for link in soup.find_all("a"):
		#Getting the href
		current = link.get("href")
		try: 
			#Checking for hrefs that ends with pdf
			if current.endswith("pdf"):
				#Write it to the file I have opened
				file.write(current + "\n")
				#Print for the console
				print(current)
				i += 1
		except:
			#In case of an error
			print('Error fetching!')
	print("Download {} links".format(i))
			
if __name__ == '__main__' : main()