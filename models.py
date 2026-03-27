class MediaItem:
    """Base class for media-related items.

    This superclass is used to demonstrate inheritance.
    """

    def __init__(self, title):
        self.title = title.strip()


class Anime(MediaItem):
    """Represents an anime series stored by the tracker."""

    def __init__(self, title, genre, total_episodes, rating):
        super().__init__(title)
        self.genre = genre.strip()
        self.total_episodes = int(total_episodes)
        self.rating = float(rating)

    def to_dict(self):
        """Convert the anime object into a dictionary for CSV writing."""
        return {
            "title": self.title,
            "genre": self.genre,
            "total_episodes": self.total_episodes,
            "rating": self.rating,
        }

    def __str__(self):
        return (
            f"Anime(title='{self.title}', genre='{self.genre}', "
            f"episodes={self.total_episodes}, rating={self.rating})"
        )


class EpisodeWatch(MediaItem):
    """Represents a watched episode entry for an anime."""

    def __init__(self, anime_title, episode_number, watched_date, duration):
        super().__init__(anime_title)
        self.anime_title = self.title
        self.episode_number = int(episode_number)
        self.watched_date = watched_date.strip()
        self.duration = int(duration)

    def to_dict(self):
        """Convert the episode entry into a dictionary for CSV writing."""
        return {
            "anime_title": self.anime_title,
            "episode_number": self.episode_number,
            "watched_date": self.watched_date,
            "duration": self.duration,
        }

    def __str__(self):
        return (
            f"EpisodeWatch(anime='{self.anime_title}', episode={self.episode_number}, "
            f"date='{self.watched_date}', duration={self.duration} mins)"
        )
