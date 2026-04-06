import requests
import src.listing as listing


#FIXME class/obj/variables name review
#FIXME self.response can be on __init__ if self.url is defined first, so its not retyped for every object


class request:
	def __init__(self, client_token):
		self.client_token = client_token
		self.header = {
			"X-MAL-CLIENT-ID": self.client_token
		}


class get_json(request):
	def user_list(self, username):
		self.username = username
		self.url = f"https://api.myanimelist.net/v2/users/{self.username}/animelist?fields=list_status&limit=10"
		self.response = (requests.get(self.url, headers=self.header)).json()
		self.data = listing.list(self.response).user_anime_list()
		return self.data
	
	def anime_request(self, anime_id):
		self.anime_id = anime_id
		self.url = f"https://api.myanimelist.net/v2/anime/{self.anime_id}?fields=num_episodes"
		self.data = listing.list((requests.get(self.url, headers=self.header)).json()).anime_list(anime_id)
		return self.data