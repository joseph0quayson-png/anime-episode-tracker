def calculate_completion_rate(watched_episodes, total_episodes):
    """Return viewing progress as a percentage."""
    if total_episodes <= 0:
        return 0.0
    return (watched_episodes / total_episodes) * 100


def find_top_rated_anime(anime_list):
    """Return the anime with the highest rating.

    Raises:
        ValueError: If the list is empty.
    """
    if not anime_list:
        raise ValueError("Anime list is empty.")
    return max(anime_list, key=lambda anime: anime.rating)
