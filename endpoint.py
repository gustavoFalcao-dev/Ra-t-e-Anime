import requests

#FIXME class name

class MSG:
	def __init__(self, username, client_token):
		self.username = username
		self.client_token = client_token
		self.header = {
			"X-MAL-CLIENT-ID": self.client_token
		}

class get_json(MSG):
	def user_list(self):
		url = f"https://api.myanimelist.net/v2/users/{self.username}/animelist?fields=list_status&limit=10"
		response = requests.get(url, headers=self.header)
		return response.json()
