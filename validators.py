import re


TITLE_PATTERN = re.compile(r"^[A-Za-z0-9 .:'!\-]{2,60}$")
GENRE_PATTERN = re.compile(r"^[A-Za-z ]{3,30}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SEARCH_PATTERN = re.compile(r"^[A-Za-z0-9 .:'!\-]{1,40}$")


def is_valid_title(title):
    """Return True if the anime title matches the expected format."""
    return bool(TITLE_PATTERN.search(title.strip()))


def is_valid_genre(genre):
    """Return True if the genre contains only letters and spaces."""
    return bool(GENRE_PATTERN.search(genre.strip()))


def is_valid_date(date_text):
    """Return True if the date follows YYYY-MM-DD format."""
    return bool(DATE_PATTERN.search(date_text.strip()))


def is_valid_title_search(keyword):
    """Return True if the search term is safe and sensible."""
    return bool(SEARCH_PATTERN.search(keyword.strip()))


def is_valid_rating(rating):
    """Validate rating range without regex because numeric rules suit logic better."""
    return 0 <= float(rating) <= 10


def is_valid_episode_count(total_episodes):
    """Check that total episode count is a positive integer."""
    return int(total_episodes) > 0


def is_valid_duration(duration):
    """Check that duration is a sensible positive number of minutes."""
    return 1 <= int(duration) <= 300
