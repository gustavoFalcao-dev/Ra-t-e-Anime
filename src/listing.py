class anime_listing:
    def __init__(self, data):
        self.entries = []
        try:
            self.data = data["data"]
        except:
            self.data = data

    def anime_list(self):
        pics = self.data.get("main_picture", [])

        self.entries.append(
            {
                "title": self.data.get("title"),
                "anime_image": pics.get("large") or pics.get("medium"),
                "episodes": self.data.get("num_episodes")
            }
        )
        return self.entries
    
    def user_anime_list(self):
        for anime in self.data:
            node = anime.get("node", anime)
            title = node.get("title")
            pics = anime.get("main_picture", {})
            list_status = anime.get("list_status", {})
            self.entries.append(
                {
                    "title": title,
                    "anime_image": pics.get("large") or pics.get("medium"),
                    "status": list_status.get("status"),
                    "score": list_status.get("score")
                }
            )
        return self.entries