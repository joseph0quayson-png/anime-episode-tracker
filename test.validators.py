from validators import (
    is_valid_title,
    is_valid_genre,
    is_valid_date,
    is_valid_title_search,
    is_valid_rating,
    is_valid_episode_count,
    is_valid_duration,
)


def test_valid_title_accepts_normal_anime_title():
    assert is_valid_title("Attack on Titan") is True


def test_valid_title_rejects_too_short_title():
    assert is_valid_title("A") is False


def test_valid_title_rejects_invalid_symbols():
    assert is_valid_title("Naruto@") is False


def test_valid_genre_accepts_letters_and_spaces():
    assert is_valid_genre("Action Adventure") is True


def test_valid_genre_rejects_numbers():
    assert is_valid_genre("Action2") is False


def test_valid_date_accepts_correct_format():
    assert is_valid_date("2026-03-26") is True


def test_valid_date_rejects_wrong_format():
    assert is_valid_date("26/03/2026") is False


def test_valid_search_accepts_keyword():
    assert is_valid_title_search("One Piece") is True


def test_valid_search_rejects_empty_string():
    assert is_valid_title_search("") is False


def test_valid_rating_limits():
    assert is_valid_rating(0) is True
    assert is_valid_rating(10) is True
    assert is_valid_rating(11) is False


def test_valid_episode_count_rules():
    assert is_valid_episode_count(12) is True
    assert is_valid_episode_count(0) is False


def test_valid_duration_rules():
    assert is_valid_duration(24) is True
    assert is_valid_duration(301) is False
