import requests
import src.listing as listing


class request:
	def __init__(self, client_token):
		self.client_token = client_token #Making the token global
		self.header = {
			"X-MAL-CLIENT-ID": self.client_token
		} #Header so the API knows which client is requesting the data

	def get_json(self, url):
		return requests.get(url, headers = self.header).json() #Function to that sends the GET request

	def user_list(self, username): #Endpoint to get the anime list of a specific user
		url = f"https://api.myanimelist.net/v2/users/{username}/animelist?fields=list_status&limit=10" #URL of the said endpoint
		return listing.anime_listing(self.get_json(url)).user_anime_list() #Returns the data :D
	
	def anime_request(self, anime_id): #Endpoint to get the data of a specific anime (through the ID)
		url = f"https://api.myanimelist.net/v2/anime/{anime_id}?fields=num_episodes" #URL of the said endpoint
		return listing.anime_listing(self.get_json(url)).anime_list() #Returns the data :D