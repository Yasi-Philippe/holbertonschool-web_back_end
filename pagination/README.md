# Pagination

This project covers different pagination strategies in Python, applied to a dataset of popular baby names (`Popular_Baby_Names.csv`).

## Tasks

### 0. Simple Helper Function — `0-simple_helper_function.py`

A standalone `index_range(page, page_size)` function that converts 1-indexed page numbers into `(start, end)` tuple indices suitable for slicing a list.

- Page 1, page_size 7 → `(0, 7)`
- Page 3, page_size 15 → `(30, 45)`

### 1. Simple Pagination — `1-simple_pagination.py`

A `Server` class with a `get_page(page, page_size)` method that:

- Loads and caches the CSV dataset (header row excluded).
- Validates that both arguments are positive integers via `assert`.
- Uses `index_range` to slice the correct rows.
- Returns an empty list when the requested page is out of range.

### 2. Hypermedia Pagination — `2-hypermedia_pagination.py`

Extends the `Server` class with `get_hyper(page, page_size)`, which returns a dictionary containing:

| Key | Description |
|---|---|
| `page` | Current page number |
| `page_size` | Number of items on this page |
| `data` | The actual rows for this page |
| `prev_page` | Previous page number, or `None` |
| `next_page` | Next page number, or `None` |
| `total_pages` | Total number of pages in the dataset |

This gives clients enough context to navigate the dataset without knowing its size in advance.

### 3. Deletion-Resilient Hypermedia Pagination — `3-hypermedia_del_pagination.py`

Extends `Server` with an `indexed_dataset` (a `dict` mapping original row index → row) and a `get_hyper_index(index, page_size)` method.

Because rows are keyed by their original index, deletions leave gaps in the dict. The method skips missing keys and collects exactly `page_size` existing rows, then reports the true `next_index` to use. This guarantees that no items are skipped when the caller pages forward, even if rows were removed between requests.

Returns:

| Key | Description |
|---|---|
| `index` | Start index of the current page |
| `next_index` | Index to pass for the next page |
| `page_size` | Requested page size |
| `data` | Actual rows collected |

## Dataset

`Popular_Baby_Names.csv` — 19 418 rows of NYC popular baby name data (year, gender, ethnicity, name, count, rank). The header row is always stripped before use.

## Usage

```bash
# Task 0
./0-main.py

# Task 1
./1-main.py

# Task 2
./2-main.py

# Task 3
./3-main.py
```

Make sure `Popular_Baby_Names.csv` is present in the same directory before running tasks 1–3.
