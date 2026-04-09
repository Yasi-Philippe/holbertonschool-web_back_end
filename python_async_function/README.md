# Python Async Function

This project covers the basics of asynchronous programming in Python using `asyncio`.

## Learning Objectives

- Understand `async` and `await` syntax
- Execute async programs with `asyncio`
- Run concurrent coroutines
- Create asyncio Tasks
- Use the `random` module with async functions

## Tasks

### 0. The basics of async
`0-basic_async_syntax.py` — Coroutine `wait_random` that waits for a random delay between 0 and `max_delay` seconds and returns it.

### 1. Execute multiple coroutines at the same time with async
`1-concurrent_coroutines.py` — Async routine `wait_n` that spawns `wait_random` n times and returns delays in ascending order using concurrency.

### 2. Measure the runtime
`2-measure_runtime.py` — Function `measure_time` that measures the total execution time of `wait_n(n, max_delay)` and returns `total_time / n`.

### 3. Tasks
`3-tasks.py` — Regular function `task_wait_random` that returns an `asyncio.Task` wrapping `wait_random`.

### 4. Tasks
`4-tasks.py` — Async function `task_wait_n` that works like `wait_n` but uses `task_wait_random` instead of `wait_random`.

## Requirements

- Python 3.7+
- All files use `#!/usr/bin/env python3`
- Type annotations are used throughout
