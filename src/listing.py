class list:
    def __init__(self, data):
        self.data = data["data"]
        self.entries = []
    
    def anime_list(self, anime_id):
        self.anime_id = anime_id
        self.pictures = self.data.get("main_pictures", {})
        self.entries.append(
            {
                "title": self.data.get("title"),
                "anime_image": self.pictures.get("large") or self.pictures.get("medium"),
                "episodes": self.data.get("num_episodes")
            }
        )
        return self.entries

    def user_anime_list(self):
        for anime in self.data:
            self.node = anime.get("node")
            if not self.node:
                return print("Not possible to request from MAL database.")
            self.statuses = anime.get("list_status", {})
            self.pictures = self.node.get("main_pictures", {})

            self.entries.append(
                {
                    "title": self.node.get("title"),
                    "anime_image": self.pictures.get("large") or self.pictures.get("medium"),
                    "status": self.statuses.get("status"),
                    "score": self.statuses.get("score")
                }
            )
        return self.entries