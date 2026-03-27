import os
import file_io
from tracker import Tracker


class TestTracker(unittest.TestCase):
    """Test suite for the Tracker class."""

    def setUp(self):
        """Create unique temporary CSV files for each test.

        This is a good testing approach because it isolates each test case and
        prevents data from one test affecting another.
        """
        import uuid

        base = tempfile.gettempdir()
        uid = uuid.uuid4().hex
        self.anime_path = os.path.join(base, f"anime_{uid}.csv")
        self.episode_path = os.path.join(base, f"ep_{uid}.csv")

        self._orig_anime = file_io.ANIME_FILE
        self._orig_episode = file_io.EPISODE_FILE

        file_io.ANIME_FILE = self.anime_path
        file_io.EPISODE_FILE = self.episode_path

        self.tracker = Tracker()

    def tearDown(self):
        """Clean up temporary files and restore original filenames."""
        file_io.ANIME_FILE = self._orig_anime
        file_io.EPISODE_FILE = self._orig_episode

        for path in (self.anime_path, self.episode_path):
            if os.path.exists(path):
                os.remove(path)

    def test_add_anime_successfully(self):
        anime = self.tracker.add_anime("Bleach", "Action", 366, 8.5)
        self.assertEqual(anime.title, "Bleach")
        self.assertEqual(len(self.tracker.list_anime()), 1)

    def test_add_duplicate_anime_raises_error(self):
        self.tracker.add_anime("Bleach", "Action", 366, 8.5)
        with self.assertRaises(ValueError):
            self.tracker.add_anime("Bleach", "Action", 366, 8.5)

    def test_add_episode_successfully(self):
        self.tracker.add_anime("Demon Slayer", "Action", 26, 9.0)
        episode = self.tracker.add_episode("Demon Slayer", 1, "2026-03-26", 24)
        self.assertEqual(episode.episode_number, 1)
        self.assertEqual(len(self.tracker.list_episodes("Demon Slayer")), 1)

    def test_add_episode_for_missing_anime_raises_error(self):
        with self.assertRaises(ValueError):
            self.tracker.add_episode("Ghost Anime", 1, "2026-03-26", 24)

    def test_search_anime_finds_partial_match(self):
        self.tracker.add_anime("Fullmetal Alchemist", "Adventure", 64, 9.2)
        self.assertEqual(len(self.tracker.search_anime("metal")), 1)

    def test_list_episodes_returns_empty_for_unknown_title(self):
        self.assertEqual(self.tracker.list_episodes("Unknown"), [])


if __name__ == "__main__":
    unittest.main()
