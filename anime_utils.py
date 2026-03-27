def normalise_title(title):
    """Return a standardised version of a title for matching.

    The tracker uses this so that searches are not affected by accidental
    differences in spacing or capital letters.
    """
    return " ".join(title.strip().lower().split())


def title_contains_keyword(title, keyword):
    """Return True if the keyword is found within a title."""
    return normalise_title(keyword) in normalise_title(title)
