import csv
        """Read anime rows from CSV and return a list of Anime objects."""
        FileManager.ensure_files_exist()
        anime_list = []
        with open(ANIME_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                anime_list.append(
                    Anime(
                        row["title"],
                        row["genre"],
                        int(row["total_episodes"]),
                        float(row["rating"]),
                    )
                )
        return anime_list

    @staticmethod
    def save_anime(anime):
        """Append one anime entry to the anime CSV file."""
        FileManager.ensure_files_exist()
        with open(ANIME_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "genre", "total_episodes", "rating"],
            )
            writer.writerow(anime.to_dict())

    @staticmethod
    def load_episodes():
        """Read watched episode rows from CSV and return EpisodeWatch objects."""
        FileManager.ensure_files_exist()
        episode_list = []
        with open(EPISODE_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                episode_list.append(
                    EpisodeWatch(
                        row["anime_title"],
                        int(row["episode_number"]),
                        row["watched_date"],
                        int(row["duration"]),
                    )
                )
        return episode_list

    @staticmethod
    def save_episode(episode):
        """Append one watched episode entry to the episode CSV file."""
        FileManager.ensure_files_exist()
        with open(EPISODE_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["anime_title", "episode_number", "watched_date", "duration"],
            )
            writer.writerow(episode.to_dict())
