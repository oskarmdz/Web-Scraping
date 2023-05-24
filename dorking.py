import requests, bs4
from bs4 import BeautifulSoup

dorks=open("dorks_sqli.txt","r")

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

bad_requests = 0

for dork in dorks:
	url = "https://www.google.es/search?q=inurl:" + dork
	response = requests.get(url,headers=headers)
	time.sleep(5)
  
	if response.status_code == 429:
		bad_requests = bad_requests+1
		print(f"GOOGLE ERROR: 429, try: {bad_requests}")
    
		if bad_requests == 10:
			break
      
	else:
		bad_requests = 0
		soup = bs4.BeautifulSoup(response.text,"html.parser")
		elements = soup.find_all('div', {'class':'yuRUbf'})
    
		for element in elements:
			tag = element.find('a')
			content = tag.get('href')
			print(content)
