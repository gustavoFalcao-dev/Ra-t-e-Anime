import requests


class MSG:
	def __init__(self, username, client_token):
		self.username = username
		self.client_token = client_token
		self.header = {
			"X-MAL-CLIENT-ID": self.client_token
		}

class user_list(MSG):
	def teste(self):
		url = f"https://api.myanimelist.net/v2/users/{self.username}/animelist?fields=list_status&limit=10"
		response = requests.get(url, headers=self.header)
		data = response.json()
		#print(data)
