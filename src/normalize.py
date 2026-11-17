"""Week 5 extension - side-effect-free normalisation functions."""


def proportions(counts: list[float]) -> list[float]:
    """Return each count divided by the total; the input is not changed.

    Raises:
        ValueError: if the total is zero (a list of zeros would look like data).
    """
    if not counts:
        raise ValueError("Cannot normalise an empty list.") 
    total = sum(counts)
    if total == 0:
        raise ValueError("Cannot normalise a list of zeros.")
    return [count / total for count in counts]


def cpm(counts: list[float], library_size: float | None = None) -> list[float]:
    """Counts per million; library_size defaults to the sum of counts."""
    if library_size is None:
        library_size = sum(counts)
    if library_size <= 0:
        raise ValueError("Cannot normalise with a zero or negative library size.")
    return [count / library_size * 1_000_000 for count in counts]
