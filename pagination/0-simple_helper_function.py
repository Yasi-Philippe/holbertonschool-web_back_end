#!/usr/bin/env python3
"""Simple helper function for pagination index range calculation."""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of (start_index, end_index) for the given page and page_size."""
    start = (page - 1) * page_size
    return (start, start + page_size)
