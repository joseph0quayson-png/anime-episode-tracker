def __init__(self):
            return

        for episode in episodes:
            print(episode)

    def _handle_search(self, args):
        if len(args) != 1:
            raise ValueError("Usage: search keyword")

        keyword = args[0]
        if not is_valid_title_search(keyword):
            raise ValueError("Search keyword contains invalid characters.")

        results = self.tracker.search_anime(keyword)
        if not results:
            print("No matches found.")
            return

        for anime in results:
            print(anime)

    def _handle_stats(self):
        anime_list = self.tracker.list_anime()
        if not anime_list:
            print("No anime saved yet.")
            return

        top_anime = find_top_rated_anime(anime_list)
        print(f"Top rated anime: {top_anime.title} ({top_anime.rating}/10)")

        for anime in anime_list:
            watched = len(self.tracker.list_episodes(anime.title))
            rate = calculate_completion_rate(watched, anime.total_episodes)
            print(f"{anime.title}: {rate:.1f}% complete")

    def _handle_export(self, args):
        if len(args) != 1:
            raise ValueError("Usage: export_summary filename.txt")

        filename = args[0]
        summary_lines = []
        for anime in self.tracker.list_anime():
            watched = len(self.tracker.list_episodes(anime.title))
            rate = calculate_completion_rate(watched, anime.total_episodes)
            summary_lines.append(
                f"{anime.title} | Genre: {anime.genre} | Rating: {anime.rating} | "
                f"Progress: {watched}/{anime.total_episodes} ({rate:.1f}%)"
            )

        with open(filename, "w", encoding="utf-8") as file:
            for line in summary_lines:
                file.write(line + "\n")

        print(f"Summary exported to {filename}")


if __name__ == "__main__":
    app = AnimeTrackerApp()
    app.run(sys.argv[1:])
