import sys
from tracker import Tracker
from validators import is_valid_title_search
from stats import calculate_completion_rate, find_top_rated_anime


HELP_TEXT = """
Anime Episode Tracker - Commands
--------------------------------
python app.py add_anime "Title" genre total_episodes rating
python app.py add_episode "Title" episode_number watched_date duration
python app.py list_anime
python app.py list_episodes "Title"
python app.py search keyword
python app.py stats
python app.py export_summary summary.txt
"""


class AnimeTrackerApp:

    def __init__(self):
        # create tracker object
        self.tracker = Tracker()

    def run(self, args):
        if not args:
            print(HELP_TEXT)
            return

        command = args[0]

        if command == "search":
            self._handle_search(args[1:])
        elif command == "stats":
            self._handle_stats()
        elif command == "export_summary":
            self._handle_export(args[1:])
        else:
            print("Command not recognised")

    def _handle_search(self, args):
        if len(args) != 1:
            raise ValueError("Usage: search keyword")

        keyword = args[0]

        if not is_valid_title_search(keyword):
            raise ValueError("Invalid search input")

        results = self.tracker.search_anime(keyword)

        if not results:
            print("No matches found")
            return

        for anime in results:
            print(anime)

    def _handle_stats(self):
        anime_list = self.tracker.list_anime()

        if not anime_list:
            print("No anime saved yet")
            return

        top = find_top_rated_anime(anime_list)
        print(f"Top rated: {top.title}")

        for anime in anime_list:
            watched = len(self.tracker.list_episodes(anime.title))
            rate = calculate_completion_rate(watched, anime.total_episodes)
            print(f"{anime.title}: {rate:.1f}%")

    def _handle_export(self, args):
        if len(args) != 1:
            raise ValueError("Usage: export_summary filename.txt")

        filename = args[0]

        with open(filename, "w") as file:
            for anime in self.tracker.list_anime():
                watched = len(self.tracker.list_episodes(anime.title))
                rate = calculate_completion_rate(watched, anime.total_episodes)

                file.write(
                    f"{anime.title} - {watched}/{anime.total_episodes} ({rate:.1f}%)\n"
                )

        print("Export complete")


if __name__ == "__main__":
    app = AnimeTrackerApp()
    app.run(sys.argv[1:])
