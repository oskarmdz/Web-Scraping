import requests, threading

username = input("Username => ")

class network:
	def __init__(self,url,username):
		self.url = url
		self.username = username

	def search(self):
		url = f"{self.url}{self.username}"
		r = requests.get(url)
		if r.status_code == 200:
			if self.url == "https://instagram.com/":
				print("usuario de instagram ",url)
			elif self.url == "https://twitter.com/":
				pass
		else:
			print("no encontrado",url)

youtube = network("https://youtube.com/@",username)
#youtube.search()
instagram = network("https://instagram.com/",username)
#instagram.search()

if __name__ == '__main__':
	t1 = threading.Thread(target=youtube.search)
	t2 = threading.Thread(target=instagram.search)
	t1.start()
	t2.start()
