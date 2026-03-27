from models import Anime, EpisodeWatch
        self.episode_list = FileManager.load_episodes()

    def add_anime(self, title, genre, total_episodes, rating):
        """Create and save an anime after validating the input."""
        if not is_valid_title(title):
            raise ValueError("Invalid anime title.")
        if not is_valid_genre(genre):
            raise ValueError("Invalid genre.")
        if not is_valid_episode_count(total_episodes):
            raise ValueError("Total episodes must be above 0.")
        if not is_valid_rating(rating):
            raise ValueError("Rating must be between 0 and 10.")
        if self._anime_exists(title):
            raise ValueError("Anime already exists.")

        anime = Anime(title, genre, total_episodes, rating)
        self.anime_list.append(anime)
        FileManager.save_anime(anime)
        return anime

    def add_episode(self, anime_title, episode_number, watched_date, duration):
        """Create and save a watched episode entry."""
        if not self._anime_exists(anime_title):
            raise ValueError("Anime title does not exist in tracker.")
        if int(episode_number) <= 0:
            raise ValueError("Episode number must be above 0.")
        if not is_valid_date(watched_date):
            raise ValueError("Date must be in YYYY-MM-DD format.")
        if not is_valid_duration(duration):
            raise ValueError("Duration must be between 1 and 300 minutes.")

        episode = EpisodeWatch(anime_title, episode_number, watched_date, duration)
        self.episode_list.append(episode)
        FileManager.save_episode(episode)
        return episode

    def list_anime(self):
        """Return all anime currently stored."""
        return list(self.anime_list)

    def list_episodes(self, anime_title):
        """Return all watched episodes for a specific anime."""
        target = normalise_title(anime_title)
        return [
            episode
            for episode in self.episode_list
            if normalise_title(episode.anime_title) == target
        ]

    def search_anime(self, keyword):
        """Return anime whose title contains the search keyword."""
        return [anime for anime in self.anime_list if title_contains_keyword(anime.title, keyword)]

    def _anime_exists(self, title):
        """Return True if an anime with the same title is already stored."""
        target = normalise_title(title)
        return any(normalise_title(anime.title) == target for anime in self.anime_list)
